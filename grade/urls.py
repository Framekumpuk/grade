from django.conf.urls import url

from . import views

app_name = 'grade'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail$', views.operand, name='operand' ),
    url(r'^show$', views.show, name='show' ),
]
