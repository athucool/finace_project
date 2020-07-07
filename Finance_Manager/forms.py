from django import forms
from .models import FinanceManager
class FinanceManagerForm(forms.ModelForm):

    class Meta:
        model = FinanceManager
        fields = ('approve_payments',)  
      