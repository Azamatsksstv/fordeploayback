from django.urls import path
from .views import PlantList, PlantDetail, ToggleLike

urlpatterns = [
    path('plants/', PlantList.as_view(), name='plant-list'),
    path('plants/<int:pk>/', PlantDetail.as_view(), name='plant-detail'),
    path('plants/<int:pk>/toggle-like/', ToggleLike.as_view(), name='toggle-like'),
]
