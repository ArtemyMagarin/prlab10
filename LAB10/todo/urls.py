from .views import index, signup
from django.conf.urls import url

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^signup/$', signup, name='signup'),

]