from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.shortcuts import render
from .controllers.rank_controller import ranking
from .forms import ProfileForm
from .models import Profile


class UserProfile(LoginRequiredMixin, TemplateView):
    template_name = 'profiles/profile.html'

    def get(self, request, **kwargs):
        user = request.user
        ranking(user)
        profile_form = ProfileForm()

        context = {
            'rank': user.rank,
            'form': profile_form,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        profile, created = Profile.objects.get_or_create(user=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)

        if profile_form.is_valid():
            profile_form.save()

        return redirect('UserProfile')
