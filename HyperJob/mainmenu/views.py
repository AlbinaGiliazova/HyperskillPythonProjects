from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views import View
from vacancy.views import VacancyForm


class MenuView(TemplateView):
    template_name = "mainmenu\\menu.html"


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'mainmenu\\signup.html'


class MyLoginView(LoginView):
    # form_class = AuthenticationForm
    redirect_authenticated_user = True
    template_name = 'mainmenu\\login.html'


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        context = {'vacancy_form': VacancyForm()}
        return render(request, 'mainmenu\\profile.html')
