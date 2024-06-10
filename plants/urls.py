from django.urls import path
from .views import PlantListCreateAPIView, PlantDetailAPIView, WateringListCreateAPIView, WateringDetailAPIView

urlpatterns = [
    path('plants/', PlantListCreateAPIView.as_view(), name='plant-list-create'),
    path('plants/<int:pk>/', PlantDetailAPIView.as_view(), name='plant-detail'),
    path('plants/<int:pk>/waterings/', WateringListCreateAPIView.as_view(), name='watering-list-create'),
    path('plants/<int:pk>/waterings/<int:id>/', WateringDetailAPIView.as_view(), name='watering-detail'),
]
