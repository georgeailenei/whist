from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from userauth.serializers import UserSerializer


class LoginInterfaceView(LoginView):
    template_name = "userauth/login.html"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home_page")
        return super().get(request, *args, **kwargs)


class LogoutInterfaceView(LogoutView):
    template_name = "userauth/logout.html"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect("home_page")
        return super().get(request, *args, **kwargs)


class SignupInterfaceView(CreateView):
    form_class = RegisterUserForm
    template_name = "userauth/register.html"
    success_url = "/success"

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect("home_page")
        return super().get(request, *args, **kwargs)


class SuccessRegistration(TemplateView):
    template_name = "userauth/success_registration.html"

    def get(self, request):
        return render(request, self.template_name)


class SelfApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, *args, **kwargs):
        return Response(data=UserSerializer(instance=self.request.user).data)
