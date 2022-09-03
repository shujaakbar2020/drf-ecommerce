from django.urls import path

from products.views import ProductList, ProductDetail, UploadfileView


urlpatterns = [
    path('', ProductList.as_view(), name='all'),
    path('detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
    # path('upload/', BulkProductsViewSet.as_view({'get': 'list'}), name='upload'),
    path('data/', UploadfileView.as_view(), name='data')
]