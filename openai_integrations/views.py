from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .oai_queries import get_completion
from .models import QuestionAnswer
from .serializers import QuestionAnswerSerializer
import requests


class QueryAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        prompt = request.data.get('prompt')
        previous_qas = QuestionAnswer.objects.filter(user=request.user)
        response = get_completion(prompt, previous_qas)

        new_qa = QuestionAnswer(user=request.user, question=prompt, answer=response)
        new_qa.save()

        return Response({'response': response})

    def get(self, request):
        previous_qas = QuestionAnswer.objects.filter(user=request.user)
        serializer = QuestionAnswerSerializer(previous_qas, many=True)
        return Response({'previous_qas': serializer.data})


class PlantIdentification(APIView):
    def post(self, request):
        image_file = request.FILES.get('image')

        if not image_file:
            return Response({"error": "No image provided"}, status=400)

        headers = {'Api-key': 'cNX6UX4KWbSYsoYOYQueHrIky8qTgJ3YHC8aHfWRIYHKmn5xfB'}
        files = {'image': image_file}
        response = requests.post('https://plant.id/api/v3/identification', headers=headers, files=files)

        try:
            data = response.json()
            plant_name = data.get('result', {}).get('classification', {}).get('suggestions', [])[0].get('name')
            return Response({"plant_name": plant_name})
        except:
            return Response({"error": "Failed to identify plant"}, status=response.status_code)
