from django.urls import path
from core.auth.views.register import UserRegisterView, TeacherRegisterView

urlpatterns = [
    path('auth/register/user/', UserRegisterView.as_view()),
    path('auth/register/teacher/', TeacherRegisterView.as_view()),
]