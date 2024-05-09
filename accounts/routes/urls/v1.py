from django.urls import path
from accounts.routes.registration.verify import VerifyOTP
from accounts.routes.registration.register import RegisterAPI
from accounts.routes.profile.changeUserInfo import MyProfileAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('accounts/register/', RegisterAPI.as_view()),
    path('accounts/verify/', VerifyOTP.as_view()),
    path('accounts/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('accounts/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('accounts/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('my_profile/', MyProfileAPIView.as_view(), name='my-profile'),
]
