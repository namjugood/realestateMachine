from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Property
from .serializers import PropertySerializer
from ..common.utils import callGetApi, get_deal_ym_range
from django.conf import settings
import logging
from estate_core.config.exceptions import ExceptionView, ParameterException, DataNotFoundException, ServerException
import re
import pandas as pd
import json

logger = logging.getLogger('estate_core')

class RealEstateViewSet(viewsets.ModelViewSet):
    """
    부동산 매물 뷰셋
    """
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'address']
    ordering_fields = ['price', 'created_at', 'area']

    def perform_create(self, serializer):
        """
        매물 생성 시 현재 로그인한 사용자를 소유자로 설정
        """
        serializer.save(owner=self.request.user)

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def getStanReginCd(self, request):
        """
        표준 지역 코드 목록을 가져오는 외부 API 호출
        @regions : str 지역명
        """
        try:
            logger.info(f"#############getStanReginCd############# {request.data}")
            if not request.data.get('regions'):
                raise ParameterException('지역명이 필요합니다.')

            params = {
                'serviceKey': settings.DATAGO_KEY,
                'pageNo': 1,
                'numOfRows': 1000,
                'locatadd_nm': request.data.get('regions'),
                'type': 'xml'
            }
            
            result = callGetApi(settings.STAN_REGIN_CD, params=params)
            if not result:
                raise DataNotFoundException('해당 지역의 데이터가 없습니다.')

            df = pd.DataFrame(result.get('row')).filter(['sido_cd', 'sgg_cd', 'umd_cd', 'ri_cd', 'locatadd_nm'])
            df['sido_sgg'] = df['sido_cd'] + df['sgg_cd']
            
            f_no_umd_cd = df['umd_cd'] == '000'
            f_no_ri_cd = df['ri_cd'] == '00'
            f_no_sgg_cd = df['sgg_cd'] != '000'
            df = df.loc[f_no_umd_cd & f_no_ri_cd & f_no_sgg_cd].sort_values(by='locatadd_nm')
            df = df.filter(['sido_sgg', 'locatadd_nm'])

            logger.info(f"#############df############# {df}")

            df = df.to_dict(orient='records')
            return ExceptionView(data=df, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"getStanReginCd 오류: {e}")
            raise ServerException(f"서버 오류가 발생했습니다: {str(e)}")

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def getRealEstateAptList(self, request):
        """
        국토교통부_아파트 매매 실거래가 상세 자료
        @region_code : str 지역코드
        @deal_ym : str 거래년월
        """
        try:
            logger.info(f"#############getRealEstateAptList############# {request.data}")
            region_code = request.data.get('region_code')
            deal_ym = request.data.get('deal_ym')

            if not region_code or not deal_ym:
                raise ParameterException('지역코드와 거래년월이 필요합니다.')
            
            # 거래년월 형식 검증
            if not re.match(r'^\d{4}\d{2}$', deal_ym):
                raise ParameterException('거래년월 형식이 올바르지 않습니다.')

            params = {
                'serviceKey': settings.DATAGO_KEY,
                'pageNo': 1,
                'numOfRows': 1000,
                'LAWD_CD': region_code,
                'DEAL_YMD': deal_ym
            }
            
            result = callGetApi(settings.RTMS_DATA_SVC_APT_TRADE_DEV, params=params)
            if not result:
                raise DataNotFoundException('해당 지역의 실거래가 데이터가 없습니다.')

            print("#############result#############", result)
            return ExceptionView(data=result, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"getRealEstateAptList 오류: {e}")
            raise ServerException(f"서버 오류가 발생했습니다: {str(e)}")
    

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def getRealEstateAptListDuration(self, request):
        """
        국토교통부_아파트 매매 실거래가 상세 자료(기간검색색)
        @region_code : str 지역코드
        @start_deal_ym : str 거래년월(시작)
        @end_deal_ym : str 거래년월(종료)
        """
        logger.info(f"#############getRealEstateAptListDuration############# {request.data}")
        try:
            region_code = request.data.get('region_code')
            start_deal_ym = request.data.get('start_deal_ym')
            end_deal_ym = request.data.get('end_deal_ym')
            pageNo = request.data.get('pageNo', 1)
            numOfRows = request.data.get('numOfRows', 1000)

            # 파라미터 검증
            if not region_code or not start_deal_ym or not end_deal_ym:
                raise ParameterException('지역코드와 거래년월이 필요합니다.')
            
            # 거래년월 형식 검증
            if not re.match(r'^\d{4}\d{2}$', str(start_deal_ym)) or not re.match(r'^\d{4}\d{2}$', str(end_deal_ym)):
                raise ParameterException('거래년월 형식이 올바르지 않습니다.')

            # 거래년월 범위 검증
            if int(start_deal_ym) > int(end_deal_ym):
                raise ParameterException('시작 거래년월이 종료 거래년월보다 클 수 없습니다.')

            # 거래년월 범위 산정
            deal_ym = get_deal_ym_range(start_deal_ym, end_deal_ym)

            params = {
                'serviceKey': settings.DATAGO_KEY,
                'pageNo': 1,
                'numOfRows': 1000,
                'LAWD_CD': region_code,
                'DEAL_YMD': deal_ym
            }
            
            resultArr = []
            totalCount = 0
            for idx, yyyymm in enumerate(deal_ym):
                print(yyyymm)
                params['DEAL_YMD'] = yyyymm
                result = callGetApi(settings.RTMS_DATA_SVC_APT_TRADE_DEV, params=params)

                if not result:
                    if idx == len(deal_ym) - 1:
                        if len(resultArr) == 0:
                            raise DataNotFoundException('해당 지역의 실거래가 데이터가 없습니다.')
                    else :
                        continue
                else :               
                    # 데이터 정제
                    items = result['body']['items']['item']
                    if not isinstance(items, list):
                        items = [items]
                    resultArr.extend(items)
                    # 총 거래 건수 추가
                    totalCount += int(result['body']['totalCount'])
            
            # 응답 형식 변경
            formatted_response = {
                "response": {
                    "header": {
                        "resultCode": "00",
                        "resultMsg": "API 호출 성공"
                    },
                    "body": {
                        "items": {
                            "item": resultArr,
                            "numOfRows": len(resultArr),
                            "pageNo": 1,
                            "totalCount": totalCount
                        }
                    }
                }
            }
            
            return Response(formatted_response, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"getRealEstateAptList 오류: {e}")
            raise ServerException(f"서버 오류가 발생했습니다: {str(e)}")
        

    