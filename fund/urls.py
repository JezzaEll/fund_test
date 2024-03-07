from django.urls import path
from .views import FundListView, FundUploadView, FundAPIListView, FundAPIDetailView

urlpatterns = [
    path('list/', FundListView.as_view(), name='fund_list'),
    path('upload/', FundUploadView.as_view(), name='fund_upload'),
    path('api/list/', FundAPIListView.as_view(), name='fund_api_list'),
    path('api/detail/<int:fund_id>/', FundAPIDetailView.as_view(), name='fund_api_detail'),
]
