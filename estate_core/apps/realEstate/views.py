from rest_framework import viewsets, filters, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Property
from .serializers import PropertySerializer
from ..common.utils import callGetApi
from django.conf import settings
import logging
from estate_core.config.exceptions import ExceptionView, ParameterException, DataNotFoundException, ServerException

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

            return ExceptionView(data=result, status=status.HTTP_200_OK)
            
        except Exception as e:
            logging.error(f"getStanReginCd 오류: {e}")
            raise ServerException(f"서버 오류가 발생했습니다: {str(e)}")

    @action(detail=False, methods=['post'], permission_classes=[AllowAny])
    def getRealEstateAptList(self, request):
        """
        국토교통부_아파트 매매 실거래가 상세 자료
        @region_code : str 지역코드
        @deal_ym : str 거래년월
        """
        try:
            region_code = request.data.get('region_code')
            deal_ym = request.data.get('deal_ym')

            if not region_code or not deal_ym:
                raise ParameterException('지역코드와 거래년월이 필요합니다.')

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

            return ExceptionView(data=result, status=status.HTTP_200_OK)
            
        except Exception as e:
            logging.error(f"getRealEstateAptList 오류: {e}")
            raise ServerException(f"서버 오류가 발생했습니다: {str(e)}")