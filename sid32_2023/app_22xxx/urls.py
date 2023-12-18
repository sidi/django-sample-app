from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('list/', views.list),
    path('department/', views.DepartmentList.as_view(), name='department_list'),
    path('department/add', views.DepartmentCreate.as_view(), name='department_create'),
    path('department/<slug:pk>', views.DepartmentDetail.as_view(), name='department_detail'),
    path('department/update/<slug:pk>', views.DepartmentUpdate.as_view(), name='department_update'),
    path('department/delete/<slug:pk>', views.DepartmentDelete.as_view(), name='department_delete'),
    path('module/', views.ModuleList.as_view(), name='module_list'),
    path('module/add', views.ModuleCreate.as_view(), name='module_create'),
    path('module/<slug:pk>', views.ModuleDetail.as_view(), name='module_detail'),
    path('module/update/<slug:pk>', views.ModuleUpdate.as_view(), name='module_update'),
    path('module/delete/<slug:pk>', views.ModuleDelete.as_view(), name='module_delete'),
]
