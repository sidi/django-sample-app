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
]
