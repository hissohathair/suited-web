#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Customer, Measurement
from .forms import CustomerForm


class CustomerList(ListView):
    template_name = 'customers/index.html'

    def get_queryset(self):
        """Return the most recently updated customers."""
        return Customer.objects.order_by('-modified_date')


class CustomerCreate(CreateView):
    model = Customer
    template_name = 'customers/create.html'
    form_class = CustomerForm


class CustomerDetail(DetailView):
    model = Customer
    template_name = 'customers/detail.html'
    form_class = CustomerForm


class CustomerUpdate(UpdateView):
    model = Customer
    template_name = 'customers/update.html'
    form_class = CustomerForm


class CustomerDelete(DeleteView):
    model = Customer
    template_name = 'customers/delete.html'
    success_url = reverse_lazy('customers:index')

