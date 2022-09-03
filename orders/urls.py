from django.urls import path

from orders.views import OrderList


urlpatterns = [
    path('', OrderList.as_view(), name='orders'),
]