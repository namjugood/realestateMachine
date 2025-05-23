# realEstateMachine/views.py
# 메인 페이지 뷰 정의
from django.shortcuts import render

def index(request):
    # 데이터 예시
    data = {
        'title': 'Welcome',
        'message': 'Hello, World!',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    
    # context 딕셔너리로 데이터 전달
    return render(request, 'index.html', context=data)