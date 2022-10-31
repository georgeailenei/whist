from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect


class LoginInterfaceView(LoginView):
    template_name = 'registration/login.html'


class LogoutInterfaceView(LogoutView):
    template_name = 'registration/logout.html'


class SignupInterfaceView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = '/success'

    # THE GET METHOD REDIRECTS AUTHENTICATED USERS TO HOME PAGE
    # DOES NOT ALLOW THEM TO SIGN UP AGAIN WHILE LOGGED IN
    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('')
        return super().get(request,  *args, **kwargs)


class SuccessRegistration(TemplateView):
    template_name = 'registration/success_registration.html'

    def get(self, request):
        return render(request, self.template_name)
