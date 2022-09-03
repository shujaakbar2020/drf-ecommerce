from django.urls import path

from shopping_cart.views import CartList


urlpatterns = [
    path('cart/', CartList.as_view(), name='cart'),
]