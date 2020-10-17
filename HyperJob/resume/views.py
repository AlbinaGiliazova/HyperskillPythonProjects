from django.views.generic.base import TemplateView
from resume.models import Resume
from django.views import View
from django.shortcuts import redirect
from django.http import HttpResponseForbidden

class MainView(TemplateView):
    template_name = "resume\\main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resumes'] = Resume.objects.all()
        return context

class NewView(View):

    def get(self, request, *args, **kwargs):
        return redirect("/home")

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        if request.user.is_staff:
            return HttpResponseForbidden()
        description = request.POST.get("description")
        author = request.user
        Resume.objects.create(description=description,
                              author=author)
        return redirect("/home")
