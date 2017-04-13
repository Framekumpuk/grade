from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^grade/', include('grade.urls')),
    url(r'^admin/', admin.site.urls),
]
