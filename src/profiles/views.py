from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/profile.html'

    def get(self, request, **kwargs):
        return render(request, self.template_name)

