from django.contrib import admin

from .models import Customer, Measurement

# Register your models here.

class MeasurementInline(admin.StackedInline):
    model = Measurement
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',   {'fields': ['first_name', 'last_name', 'email_address']}),
        ('Stats',  {'fields': ['age', 'height', 'weight'], 'classes': ['collapse']}),
    ]
    inlines = [MeasurementInline]
    list_display = ('first_name', 'last_name', 'age', 'email_address')
    #list_filter = ['modified_date']
    search_fields = ['first_name', 'last_name']

admin.site.register(Customer, CustomerAdmin)

