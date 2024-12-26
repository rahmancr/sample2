from django.core.management.base import BaseCommand
from faker import Faker
from tablesprgm import tabless
# from tabless.models import Customerdetails

class Command(BaseCommand):
    help = 'Generate random customer details'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):  # Adjust the range to generate more or fewer customers
            customer = Customerdetails(
                username=fake.user_name(),
                password=fake.password(),
                mobile_number=fake.phone_number(),
                place=fake.city(),
                age=fake.random_int(min=18, max=90)
            )
            customer.save()
        self.stdout.write(self.style.SUCCESS('Successfully generated random customer details'))
