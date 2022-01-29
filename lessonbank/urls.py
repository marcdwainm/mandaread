from django.urls import path
from . import views

urlpatterns = [
    path('', views.LessonsListView.as_view(), name='mandaread-lessons'),
    path('<slug:pk>/', views.LessonListDetailView.as_view(), name='mandaread-lesson'),
    path('<slug:pk>/assessment/', views.LessonAssessmentView.as_view(), name='mandaread-assessment')
]
