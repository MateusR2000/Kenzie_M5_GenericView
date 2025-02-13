from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("users/", views.ListCreateUserView.as_view()),
    path("users/<int:pk>/", views.RetrieveUpdateDestroyUserView.as_view()),
    path("users/login/", jwt_views.TokenObtainPairView.as_view()),
]
