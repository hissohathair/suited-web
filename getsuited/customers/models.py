import datetime

from django.utils import timezone
from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(blank=True)

    age = models.PositiveSmallIntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    created_date = models.DateTimeField('date created', auto_now_add=True)
    modified_date = models.DateTimeField('date modified', auto_now=True)

    def was_updated_recently(self):
        return self.modified_date >= timezone.now() - datetime.timedelta(days=3)
    was_updated_recently.admin_order_field = 'modified_date'
    was_updated_recently.boolean = True
    was_updated_recently.short_description = 'Updated recently?'

    def __str__(self):
        return "{0} {1} (#{2})".format(self.first_name, self.last_name, self.id)


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
