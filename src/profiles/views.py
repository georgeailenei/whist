from django.shortcuts import render


def user_profile_view(request):
    return render(request, 'templates/profile.html')
