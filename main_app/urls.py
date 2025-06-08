from django.urls import path
from . import views

app_name = 'main_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('all_gpu_gigabyte/', views.all_gpu_gigabyte, name='all_gpu_gigabyte'),
    path('gpu_12gb_gigabyte/', views.gpu_12gb_gigabyte, name='gpu_12gb_gigabyte'),
    path('gpu_8gb_gigabyte/', views.gpu_8gb_gigabyte, name='gpu_8gb_gigabyte'),
    path('mb_gigabyte/', views.mb_gigabyte, name='mb_gigabyte'),
    path('top_gigabyte/', views.top_gigabyte, name='top_gigabyte'),
    path('top_asus/', views.top_asus, name='top_asus'),
    path('top_msi/', views.top_msi, name='top_msi'),
    path('all_gpu_msi/', views.all_gpu_msi, name='all_gpu_msi'),
    path('gpu_12gb_msi/', views.gpu_12gb_msi, name='gpu_12gb_msi'),
    path('gpu_8gb_msi/', views.gpu_8gb_msi, name='gpu_8gb_msi'),
    path('mb_msi/', views.mb_msi, name='mb_msi'),
    path('all_gpu_asus/', views.all_gpu_asus, name='all_gpu_asus'),
    path('gpu_12gb_asus/', views.gpu_12gb_asus, name='gpu_12gb_asus'),
    path('gpu_8gb_asus/', views.gpu_8gb_asus, name='gpu_8gb_asus'),
    path('mb_asus/', views.mb_asus, name='mb_asus'),
]
