# Django modules
from django.urls import path

# Django locals
from .views import cart_page

# App name
app_name = 'carts'

urlpatterns = [
    path('', cart_page, name='cart_page'),
]