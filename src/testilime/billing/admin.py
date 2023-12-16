from django.contrib import admin
from testilime.billing.models import StripeCustomer

admin.site.register(StripeCustomer)
