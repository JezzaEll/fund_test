from django.urls import path
from .views import fund_list, fund_upload, fund_api_list, fund_api_detail

urlpatterns = [
    path('list/', fund_list, name='fund_list'),
    path('upload/', fund_upload, name='fund_upload'),
    path('api/list/', fund_api_list, name='fund_api_list'),
    path('api/detail/<int:fund_id>/', fund_api_detail, name='fund_api_detail'),
]
