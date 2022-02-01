from django.urls import path
from . import views

urlpatterns = [
    path('', views.LessonsListView.as_view(), name='mandaread-lessons'),
    path('<int:pk>/', views.LessonListDetailView.as_view(), name='mandaread-lesson'),
    path('<int:pk>/assessment/', views.LessonAssessmentView.as_view(), name='mandaread-assessment'),
]
