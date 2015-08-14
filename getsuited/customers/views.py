from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Customer, Measurement


class IndexView(generic.ListView):
    template_name = 'customers/index.html'

    def get_queryset(self):
        """Return the most recently updated customers."""
        return Customer.objects.order_by('-modified_date')


class DetailView(generic.DetailView):
    model = Customer
    template_name = 'customers/detail.html'


def update(request, customer_id):
    customer = get_object_or_404(Customer, pk=customer_id)

    details_changed = False
    for k in ('age', 'height', 'weight'):
        if k in request.POST:
            setattr(customer, k, request.POST[k])
            details_changed = True

    if details_changed:
        try:
            customer.save()
        except ValueError:
            return render(request, 'customers/detail.html', {
                    'customer': customer,
                    'error_message': "Invalid value in form",
                    })
        else:
            return HttpResponseRedirect(reverse('customers:detail', args=(customer.id,)))

    else:
        return render(request, 'customers/detail.html',  { 'customer': customer })
