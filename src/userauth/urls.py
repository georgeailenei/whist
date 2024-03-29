from django.urls import path
from . import views


urlpatterns = [
    path("login", views.LoginInterfaceView.as_view(), name="login"),
    path("logout", views.LogoutInterfaceView.as_view(), name="logout"),
    path("signup", views.SignupInterfaceView.as_view(), name="signup"),
    path("success", views.SuccessRegistration.as_view()),
    path("users/self", views.SelfApiView.as_view(), name="self"),
]
