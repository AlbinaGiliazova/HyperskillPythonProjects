from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("mainmenu.urls")),
    re_path('resumes/?', include("resume.urls")),
    re_path('vacancies/?', include("vacancy.urls")),
    re_path('resume/?', include("resume.urls")),
    re_path('vacancy/?', include("vacancy.urls")),
]

urlpatterns += static(settings.STATIC_URL)
