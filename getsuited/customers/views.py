from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse

from .models import Customer, Measurement


def index(request):
    latest_customer_list = Customer.objects.order_by('-modified_date')
    context = { 'latest_customer_list': latest_customer_list }
    return render(request, 'customers/index.html', context)


def detail(request, customer_id):
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


def measurements(request, customer_id):
    return HttpResponse("You're looking at the measurements for customer %s." % customer_id)

