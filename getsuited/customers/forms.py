from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML
from crispy_forms.bootstrap import FormActions

from .models import Customer


class CustomerForm(forms.ModelForm):
    """Model Customer form"""
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email_address', 'age', 'height', 'weight']

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.layout.append(
            FormActions(
                HTML("""<a role="button" class="btn btn-default" href="{% url 'customers:index' %}">Cancel</a>"""),
                Submit('save', 'Submit'),
                ))


