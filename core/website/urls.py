from django.urls import path
from .views import HomeView,go_to_gateway_view
app_name = 'website'

urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('gateway/',go_to_gateway_view,name = 'gateway')
]
