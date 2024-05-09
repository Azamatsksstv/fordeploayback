from django.urls import path
from .views import QueryAPIView, PlantIdentification

urlpatterns = [
    path('ai/', QueryAPIView.as_view(), name='query'),
    path('identify-plant/', PlantIdentification.as_view(), name='identify-plant'),
]
