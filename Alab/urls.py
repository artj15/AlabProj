from django.contrib import admin
from django.urls import path
from .views import ProductApi, ProductCount
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('total-cost/', ProductCount.as_view()),
]

router = DefaultRouter()
router.register(r'resources', ProductApi)
urlpatterns += router.urls