from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.shortcuts import render
from .controllers.rank_controller import ranking


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/profile.html'

    def get(self, request, **kwargs):
        user = request.user
        rank = ranking(user)

        context = {
            'rank': rank,
        }

        return render(request, self.template_name, context)
