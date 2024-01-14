from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('currency/', views.CurrencyList.as_view(), name='currency_list'),
    path('currency/add', views.CurrencyCreate.as_view(), name='currency_create'),
    path('currency/<slug:pk>', views.CurrencyDetail.as_view(), name='currency_detail'),
    path('currency/update/<slug:pk>', views.CurrencyUpdate.as_view(), name='currency_update'),
    path('currency/delete/<slug:pk>', views.CurrencyDelete.as_view(), name='currency_delete'),
    path('rate/', views.RateList.as_view(), name='rate_list'),
    path('rate/add', views.RateCreate.as_view(), name='rate_create'),
    path('rate/<slug:pk>', views.RateDetail.as_view(), name='rate_detail'),
    path('rate/update/<slug:pk>', views.RateUpdate.as_view(), name='rate_update'),
    path('rate/delete/<slug:pk>', views.RateDelete.as_view(), name='rate_delete'),

    path('import/currency', views.import_currency_csv, name='currency_import'),
    path('import/rate', views.import_rate_csv, name='rate_import'),
]
