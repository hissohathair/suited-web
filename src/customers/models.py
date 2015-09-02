# customers/models.py
# Copyright 2015 Suited Pty Ltd.

import datetime

from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.utils import timezone

from dirtyfields import DirtyFieldsMixin
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


class Customer(models.Model):
    """
    Stores a single customer's core details (name, email, height, weight & age).
    A customer has zero or more :model:`customers.Measurement`s. They may also be
    linked to zero or one :model:`auth.User` account, since it's possible for a
    Customer to exists here but to have never signed up (a service rep may have
    created the Customer).
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
    stripe_account = models.CharField(max_length=200, null=True, blank=True)

    age = models.PositiveSmallIntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    created_date = models.DateTimeField('date created', auto_now_add=True)
    modified_date = models.DateTimeField('date modified', auto_now=True)


    def get_or_create_stripe_account(self):
        """
        Returns the Customer's stripe account ID if it already exists. Otherwise,
        calls Stripe to create one and then returns that.
        """
        if self.stripe_account is None or self.stripe_account == '':
            print("Creating new stripe customer for %s" % self)
            new_stripe_id = stripe.Customer.create(email=self.email_address)
            self.stripe_account = new_stripe_id['id']
            self.save()

        return self.stripe_account


    def current_measurements(self):
        """
        Returns the current valid measurements for the customer. A customer may have more
        than one set of measurements, but only one set should be "current" at a time.
        """
        m = self.measurement_set.filter(disabled_date__isnull=True)
        if not m:
            # create an empty measurement set
            m = [Measurement(customer=self)]

        return m[0]


    def was_updated_recently(self):
        """Declares if the customer record has been edited in the last few days."""
        now = timezone.now()
        return now - datetime.timedelta(days=3) <= self.modified_date <= now
    was_updated_recently.admin_order_field = 'modified_date'
    was_updated_recently.boolean = True
    was_updated_recently.short_description = 'Updated recently?'


    def __str__(self):
        if self.stripe_account:
            return "{0} {1} ({2})".format(self.first_name, self.last_name, self.stripe_account)
        else:
            return "{0} {1} (#{2})".format(self.first_name, self.last_name, self.id)


    def get_absolute_url(self):
        return reverse('customers:detail', kwargs={'pk': self.pk})


class Measurement(DirtyFieldsMixin, models.Model):
    """
    Stores a complete set of measurements for a Customer. There may be multiple
    measurement sets taken, but only one should be active at a time. Customer
    Orders will be linked to the exact measurement set that existed when the Order
    was placed.
    """
    customer = models.ForeignKey(Customer)
    created_date = models.DateTimeField('date created', auto_now_add=True)
    modified_date = models.DateTimeField('date modified', auto_now_add=True)
    disabled_date = models.DateTimeField('date disabled', blank=True, null=True)

    shoulder_neck_shoulder = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    top_of_shoulder_to_wrist = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    bicep_under_armpit = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    mid_shoulder = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    low_shoulder = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    front_chest = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    neck_to_jacket_length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    full_chest_under_armpit = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    stomach = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    hip = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    waist_just_above_belt = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    u_crotch = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    thigh = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    trouser_length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    trouser_cuff = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    top_of_shoulder_to_fist = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fist = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    neck_to_shirt_length = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    collar = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return "{0}'s measurements".format(self.customer.first_name)


