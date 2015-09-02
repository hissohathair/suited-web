from django.contrib import admin

from .models import Customer, Measurement

class MeasurementInline(admin.StackedInline):
    model = Measurement
    fieldsets = [
        ('Suit',    {'fields': ['shoulder_neck_shoulder', 'top_of_shoulder_to_wrist', 'bicep_under_armpit',
                                'mid_shoulder', 'low_shoulder', 'front_chest', 'neck_to_jacket_length',
                                'full_chest_under_armpit', 'stomach', 'hip'],
                     'classes': ['collapse']}),
        ('Trouser', {'fields': ['waist_just_above_belt', 'hip', 'u_crotch', 'thigh', 
                                'trouser_length', 'trouser_cuff'],
                     'classes': ['collapse']}),
        ('Shirt',   {'fields': ['shoulder_neck_shoulder', 'top_of_shoulder_to_fist', 'fist', 
                                'bicep_under_armpit', 'mid_shoulder', 'front_chest', 'neck_to_shirt_length',
                                'full_chest_under_armpit', 'stomach', 'hip', 'collar'],
                     'classes': ['collapse']}),
        ]
    extra = 0

class CustomerAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',    {'fields': ['first_name', 'last_name', 'email_address']}),
        ('Stats',   {'fields': ['age', 'height', 'weight'], 'classes': ['collapse']}),
        ('Account', {'fields': ['user', 'stripe_account'], 'classes': ['collapse']}),
    ]
    inlines = [MeasurementInline]
    list_display = ('first_name', 'last_name', 'age', 'email_address', 'stripe_account')
    #list_filter = ['modified_date']
    search_fields = ['first_name', 'last_name']

admin.site.register(Customer, CustomerAdmin)


