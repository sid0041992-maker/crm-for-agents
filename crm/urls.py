from django.contrib import admin
from django.urls import path
from agents import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apartment/', views.apartment_detail),
]