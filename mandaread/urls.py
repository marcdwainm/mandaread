from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='mandaread-home'),
    path('editprofile/', views.updateProfile, name='mandaread-edit-profile'),
    path('editprofile/updatepass', views.NewPasswordChangeView.as_view(template_name='mandaread/update-pass.html'), name='mandaread-update-pass'),
    path('editprofile/deleteaccount', views.deleteAccount, name='mandaread-delete-acc'),
    path('editprofile/accountdelete', views.accountDelete, name='mandaread-acc-deleted'),
]