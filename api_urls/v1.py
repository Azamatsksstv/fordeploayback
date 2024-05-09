from django.urls import path, include


urlpatterns = [
    path('', include('accounts.routes.urls.v1')),
    path('', include('openai_integrations.urls')),
]