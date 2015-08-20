# customers.urls

from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import views

urlpatterns = [
    url(r'^$', views.CustomerList.as_view(), name='index'),
    url(r'^create/$', views.CustomerCreate.as_view(), name='create'),
    url(r'^(?P<pk>[0-9]+)/$', views.CustomerDetail.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/update/$', views.CustomerUpdate.as_view(), name='update'),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.CustomerDelete.as_view(), name='delete'),
]
