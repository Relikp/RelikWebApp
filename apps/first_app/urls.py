from django.conf.urls import url
from . import views           


urlpatterns = [
    url(r'^$', views.index), 
    url(r'^add_user$', views.add_user),
    url(r'^back_to_registration$', views.back_to_registration),
    url(r'^login$', views.login),
    url(r'^quotes$', views.quotes),
    url(r'^logout$', views.logout),
    url(r'^add_quote$', views.add_quote),
    url(r'^remove_quote/(?P<id>\d+)$', views.remove_quote),
    url(r'^user_info/(?P<id>\d+)$', views.user_info),
    url(r'^liked_quote/(?P<id>\d+)$', views.liked_quote),
]                            
