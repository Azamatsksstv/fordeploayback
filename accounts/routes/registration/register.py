from rest_framework.views import APIView
from rest_framework.response import Response

from accounts.serializers.user import UserSerializer
from accounts.emails import send_otp_via_email


class RegisterAPI(APIView):

    def post(self, request):
        try:
            data = request.data
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                send_otp_via_email(serializer.data['email'])
                return Response({
                    'status': 200,
                    'message': 'Registration successfully, check email',
                    'data': serializer.data,
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)

        return Response({
            'status': 400,
            'message': 'Something went wrong',
        })
