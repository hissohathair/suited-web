import csv

from django.core.management.base import BaseCommand, CommandError
from customers.models import Customer, Measurement

class Command(BaseCommand):
    help = 'Imports customer measurements from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        for filename in options['filename']:
            self.stdout.write('Importing %s' % filename)
            self.import_file(filename)

    def import_file(self, filename):
        with open(filename, 'r') as csvfile:
            csvread = csv.DictReader(csvfile)
            for row in csvread:
                self.import_customer(row)
        return

    def import_customer(self, custrow):
        c = Customer.objects.filter(first_name=custrow['First Name'], last_name=custrow['Last Name'])
        if c:
            self.stdout.write('  - %s already exists -- skipping' % custrow['Customer Name'])
        else:
            self.stdout.write('  - Creating %s' % custrow['Customer Name'])
            c = Customer()
            m = Measurement()

            for k, v in custrow.items():
                if k == 'Customer Name' or (not v):
                    continue

                km = k.lower().replace('-', '').replace(' ', '_').replace('__', '_')
                if hasattr(c, km):
                    setattr(c, km, v)
                elif hasattr(m, km):
                    setattr(m, km, v)
                else:
                    raise ValueError('Unexpected attribute %s (%s)' % (km, k))

            c.save()
            m.customer = c
            m.save()

        return

                
            




