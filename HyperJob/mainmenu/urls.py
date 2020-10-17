from django.urls import path, re_path
from mainmenu.views import MenuView, MySignupView, \
    MyLoginView, ProfileView

urlpatterns = [
    path('', MenuView.as_view()),
    re_path('signup/?', MySignupView.as_view()),
    re_path('login/?', MyLoginView.as_view()),
    re_path('home/?', ProfileView.as_view()),
]
