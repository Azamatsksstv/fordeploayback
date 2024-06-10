from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Plant, Watering
from .serializers import PlantSerializer, WateringSerializer
from django.shortcuts import get_object_or_404


class PlantListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        plants = Plant.objects.filter(user=request.user)
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk, user=request.user)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)

    def delete(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk, user=request.user)
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WateringListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk, user=request.user)
        waterings = Watering.objects.filter(plant=plant)
        serializer = WateringSerializer(waterings, many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        plant = get_object_or_404(Plant, pk=pk, user=request.user)
        serializer = WateringSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(plant=plant)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WateringDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk, id):
        plant = get_object_or_404(Plant, pk=pk, user=request.user)
        watering = get_object_or_404(Watering, pk=id, plant=plant)
        watering.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
