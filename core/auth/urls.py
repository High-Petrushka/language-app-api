from django.urls import path
from core.auth.views.register import UserRegisterView, TeacherRegisterView
from core.auth.views.login import UserLoginView, TeacherLoginView

urlpatterns = [
    path('auth/register/user/', UserRegisterView.as_view()),
    path('auth/register/teacher/', TeacherRegisterView.as_view()),
    path('auth/login/user/', UserLoginView.as_view()),
    path('auth/login/teacher/', TeacherLoginView.as_view()),
]