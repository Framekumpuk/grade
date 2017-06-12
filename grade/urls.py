from django.conf.urls import url

from . import views

app_name = 'grade'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^signin$', views.signin, name='signin'),
    url(r'keepuser&', views.keepUser, name='keepuser'),
    url(r'^index$', views.index, name='index'),
    url(r'^detail$', views.operand, name='operand' ),
    url(r'^show$', views.show, name='show' ),
    url(r'^about$', views.about, name='about' ),
]
