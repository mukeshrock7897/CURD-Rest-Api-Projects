from django import forms
from Employee1.models import EmployeeProfile

class EmployeeForm(forms.ModelForm):

    class Meta:
        model=EmployeeProfile
        fields="__all__"


