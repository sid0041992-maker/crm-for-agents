from django.contrib import admin
from django.urls import path
from agents import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.apartment_list, name='apartment_list'),
    path('apartment/<int:id>/', views.apartment_detail, name='apartment_detail'),
    path('deal/<int:id>/', views.deal_detail, name='deal_detail'),
]