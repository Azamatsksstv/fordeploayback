from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Plant
from .serializers import PlantSerializer


class PlantList(APIView):
    def get(self, request):
        plants = Plant.objects.all()
        serializer = PlantSerializer(plants, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PlantDetail(APIView):
    def get_object(self, pk):
        try:
            return Plant.objects.get(pk=pk)
        except Plant.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        plant = self.get_object(pk)
        serializer = PlantSerializer(plant)
        return Response(serializer.data)

    def delete(self, request, pk):
        plant = self.get_object(pk)
        plant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ToggleLike(APIView):
    def post(self, request, pk):
        plant = Plant.objects.get(pk=pk)
        plant.is_liked = not plant.is_liked
        plant.save()
        return Response(status=status.HTTP_200_OK)
