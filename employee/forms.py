from django import forms
from .models import Employee


class ProductForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'project', 'experience']

