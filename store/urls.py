from django.urls import path
from . import views

app_name='store'

urlpatterns = [

    path('',views.index, name = 'home'), 
    path('store',views.store, name = 'store'), 
    path('store/<slug:category_slug>/', views.store, name='product_list_by_category'),
    path('store/<slug:category_slug>/<slug:product_slug>/', views.detail_page, name='product_detail'),
]
    # path('route_name/<str:slug_variable>',views.route_function, name = 'reoute_name'),
