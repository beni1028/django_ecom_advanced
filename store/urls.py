from django.urls import path
from . import views

app_name='store'

urlpatterns = [

    path('',views.index, name = 'home'), 
    # path('route_name/<str:slug_variable>',views.route_function, name = 'reoute_name'),
]