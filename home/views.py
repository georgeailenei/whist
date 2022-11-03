from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get(self, request):
        ceva = False
        name = request.user
        if request.user.is_authenticated:
            ceva = True
        content = {'ceva': ceva, 'username': name}
        return render(request, self.template_name, content)
