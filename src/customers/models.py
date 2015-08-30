import datetime

from django.core.urlresolvers import reverse
from django.conf import settings
from django.db import models
from django.utils import timezone

from allauth.account.signals import user_logged_in, user_signed_up
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(blank=True)

    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)

    age = models.PositiveSmallIntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    created_date = models.DateTimeField('date created', auto_now_add=True)
    modified_date = models.DateTimeField('date modified', auto_now=True)

    def was_updated_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=3) <= self.modified_date <= now
    was_updated_recently.admin_order_field = 'modified_date'
    was_updated_recently.boolean = True
    was_updated_recently.short_description = 'Updated recently?'

    def __str__(self):
        return "{0} {1} (#{2})".format(self.first_name, self.last_name, self.id)


    def get_absolute_url(self):
        return reverse('customers:detail', kwargs={'pk': self.pk})


class UserStripe(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    stripe_id = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        if self.stripe_id:
            return str(self.stripe_id)
        else:
            return self.user.username


class Measurement(models.Model):
    customer = models.ForeignKey(Customer)
    created_date = models.DateTimeField('date created', auto_now_add=True)
    modified_date = models.DateTimeField('date modified', auto_now_add=True)

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


def stripe_callback(sender, request, user, **kwargs):
    stripe_user_account, created = UserStripe.objects.get_or_create(user=user)
    if created:
        print("Created for %s" % user.username)
    else:
        print("Fetched for %s" % user.username)

    if stripe_user_account.stripe_id is None or stripe_user_account.stripe_id == '':
        print("Creating new stripe customer...")
        new_stripe_id = stripe.Customer.create(email=user.email)
        stripe_user_account.stripe_id = new_stripe_id['id']
        stripe_user_account.save()
    else:
        print("Stripe customer already exists: %s" % stripe_user_account.stripe_id)

def customer_callback(sender, request, user, **kwargs):
    customer, created = Customer.objects.get_or_create(user=user)
    if created:
        print("Created Customer for %s" % user.username)
    else:
        print("Fetched Customer for %s" % user.username)

user_logged_in.connect(stripe_callback)
user_signed_up.connect(stripe_callback)
user_signed_up.connect(customer_callback)

