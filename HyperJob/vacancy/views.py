from django.views.generic.base import TemplateView
from vacancy.models import Vacancy
from django.views import View
from django.shortcuts import redirect
from django.http import HttpResponseForbidden
from django import forms


class MainView(TemplateView):
    template_name = "vacancy\\main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vacancies'] = Vacancy.objects.all()
        return context

class NewView(View):

    def get(self, request, *args, **kwargs):
        return redirect("/home")

    def post(self, request, *args, **kwargs):
        new_form = VacancyForm(request.POST)
        if request.user.is_staff:
            if new_form.is_valid():
                Vacancy.objects.create(author=request.user, description=new_form.cleaned_data['description'])
                return redirect('/home')
            return redirect("/home")
        return HttpResponseForbidden('<h1>403 Forbidden</h1>', content_type='text/html')

class VacancyForm(forms.Form):
    description = forms.CharField(label='Description', max_length=1024)
