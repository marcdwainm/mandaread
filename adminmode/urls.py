from django.urls import path, include
from . import views

urlpatterns = [
    # Lesson Management URLs
    path('', views.AdminHome.as_view(), name='admin-home'),
    path('lessons/', views.AdminLessons.as_view(), name='admin-lessons'),
    path('lessons/<int:pk>/', views.AdminLesson.as_view(), name='admin-lesson'),
    path('lessons/new/', views.AdminCreateLesson.as_view(), name='admin-create-lesson'),
    path('lessons/<int:pk>/update/', views.AdminUpdateLesson.as_view(), name='admin-update-lesson'),
    path('lessons/<int:pk>/delete/', views.AdminDeleteLesson.as_view(), name='admin-delete-lesson'),

    #Dictionary
    path('dictionary/', views.AdminDictionary.as_view(), name='admin-dict'),
    path('dictionary/createword', views.AdminCreateDictionary.as_view(), name='admin-create-dict'),
    path('dictionary/editword/<int:pk>', views.AdminUpdateDictionary.as_view(), name='admin-update-dict'),
    path('dictionary/deleteword/<int:pk>', views.AdminDeleteDictionary.as_view(), name='admin-delete-dict')
]
