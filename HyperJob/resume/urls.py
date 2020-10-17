from django.urls import path, re_path
from resume.views import MainView, NewView

urlpatterns = [
    path('', MainView.as_view()),
    re_path('new/?', NewView.as_view()),
]
