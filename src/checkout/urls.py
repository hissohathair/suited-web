# checkout.urls

from django.conf.urls import url
from django.core.urlresolvers import reverse

from . import views

urlpatterns = [
    url(r'^$', 'checkout.views.checkout', name='checkout'),
]
