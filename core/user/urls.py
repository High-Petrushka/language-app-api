from django.urls import path

from core.user.views import UserProfileView

urlpatterns = [
    path('user/<int:pk>/', UserProfileView.as_view()),
]