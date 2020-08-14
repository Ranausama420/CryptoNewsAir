from django.urls import path

from . import views
app_name = 'CryptoNewsWebsite'


urlpatterns = [
    path('', views.index, name='index'),
    path('News/Article/<str:title>/', views.singlepost, name='single-post'),
    path('News/<str:title>/', views.catagory, name='catagory'),
    path('Videos/<str:title>/', views.videos, name='videos'),
    path('Coins/?Page=<int:page>/', views.marketcap, name='marketcap'),
    path('Exchanges/?Page=<int:page>/', views.exchange, name='exchange'),



]