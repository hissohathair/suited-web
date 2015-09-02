import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Customer, Measurement


class CustomerMethodTests(TestCase):

    def test_created_customer_has_measurents(self):
        """
        current_measurements() should return a new measurement record for
        a new customer.
        """
        c = Customer(first_name="test", last_name="test")
        c.save()
        m = c.current_measurements()
        self.assertTrue(isinstance(m, Measurement))


    def test_was_updated_recently_future_date(self):
        """
        was_modified_recently() should return False for future dates.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_customer = Customer(modified_date=time)
        self.assertEqual(future_customer.was_updated_recently(), False)

    def test_was_updated_recently_old_date(self):
        """
        was_modified_recently() should return False for customers
        edited longer than 3 days ago.
        """
        time = timezone.now() - datetime.timedelta(days=4)
        old_customer = Customer(modified_date=time)
        self.assertEqual(old_customer.was_updated_recently(), False)

    def test_was_updated_recently_recent_date(self):
        """
        was_modified_recently() should return True for customers
        edited within last 3 days.
        """
        time = timezone.now() - datetime.timedelta(days=2)
        new_customer = Customer(modified_date=time)
        self.assertEqual(new_customer.was_updated_recently(), True)


