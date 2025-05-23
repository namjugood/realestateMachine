from django.urls import path
from . import views

# API URL 설정
urlpatterns = [
    path('data/', views.real_estate_data, name='real_estate_data'),
] 