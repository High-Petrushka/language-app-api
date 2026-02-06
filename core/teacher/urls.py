from django.urls import path
from core.teacher.views import TeachersView, TeacherProfileView

urlpatterns = [
    path('teachers/', TeachersView.as_view()),
    path('teachers/<int:pk>/', TeacherProfileView.as_view()),
]