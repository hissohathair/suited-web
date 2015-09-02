from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
    publish_key = settings.STRIPE_PUBLISHABLE_KEY
    customer_id = request.user.customer.get_or_create_stripe_account()
    if request.method == 'POST':
        token = request.POST['stripeToken']

        # Create the charge on Stripe's servers - this will charge the user's card
        try:
            customer = stripe.Customer.retrieve(customer_id)
            customer.sources.create(source=token)
            charge = stripe.Charge.create(
                amount=1000, # amount in cents, again
                customer=customer,
                currency="aud",
                description="Example charge"
                )
        except(stripe.error.CardError) as e:
            # The card has been declined
            pass

    context = { 'publish_key': publish_key }
    template = 'checkout/index.html'
    return render(request, template, context)



