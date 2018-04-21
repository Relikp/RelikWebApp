from django.conf.urls import url
from . import views           


urlpatterns = [
    url(r'^$', views.index), 
    url(r'^add_user$', views.add_user),
    url(r'^login$', views.login),
    url(r'^success$', views.success),
    url(r'^back_to_registration$', views.back_to_registration),
]                            
