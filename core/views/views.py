# core/views/views.py
# 메인 페이지 뷰 정의
from django.shortcuts import render
from django.http import JsonResponse
from datakart import Datagokr
from django.conf import settings

import pandas as pd

def index(request):
    # 데이터 예시
    data = {
        'title': 'Welcome',
        'message': 'Hello, World!',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    
    # context 딕셔너리로 데이터 전달
    return render(request, 'index.html', context=data)

# 서울특별시 시 코드 가져오기
def getStanReginCd(request):
    try:
        region = request.GET.get('region', '서울특별시')
        datago = Datagokr(settings.DATAGO_KEY)
        result = datago.lawd_code(region)
        
        # 데이터 프레임 생성
        df = pd.DataFrame(result).filter(["sido_cd", "sgg_cd", "umd_cd", "ri_cd", "locatadd_nm"])
        
        # 컬럼 추가 및 데이터 전처리
        df["sido_sgg"] = df["sido_cd"] + df["sgg_cd"]

        f_no_umd = df["umd_cd"] == "000"
        f_no_ri = df["ri_cd"] == "00"
        f_sgg = df["sgg_cd"] != "000"

        df = df.loc[f_no_umd & f_no_ri & f_sgg]
        df = df.filter(["sido_sgg", "locatadd_nm"]).sort_values(by="locatadd_nm")

        print("DataFrame 정보:")
        print(df.info())
        print("\nDataFrame 미리보기:")
        print(df.head())
        
        
        # DataFrame을 JSON 형식으로 변환
        json_data = df.to_dict(orient='records')
        return JsonResponse({
            'status': 'success',
            'data': json_data
        })
        
    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)
    
# 아파트 실거래가 가져오기
def getAptRealEstate(request):
    try:
        datago = Datagokr(settings.DATAGO_KEY)
        result = datago.apt_trade("11680", "202501")
        
        df = pd.DataFrame(result)

        
        # 디버그 출력
        print("\n=== DataFrame 정보 ===")
        print(f"데이터 개수: {len(df)}")
        print(f"컬럼 개수: {len(df.columns)}")
        print(df.info())
        print("\n=== DataFrame 미리보기 ===")
        print(df.head())
        
        json_data = df.to_dict(orient='records')
        return JsonResponse({
            'status': 'success',
            'data': json_data
        })
    except Exception as e:
        print(f"\n=== 에러 발생 ===\n{str(e)}")
        return JsonResponse({
            'status': 'error',
            'message': str(e)
        }, status=400)