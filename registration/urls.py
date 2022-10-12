from django.urls import path
from . import views


urlpatterns = [
    path('login', views.LoginInterfaceView.as_view()),
    path('logout', views.LogoutInterfaceView.as_view()),
    path('signup', views.SignupInterfaceView.as_view()),
    path('success', views.SuccessRegistration.as_view()),
]
