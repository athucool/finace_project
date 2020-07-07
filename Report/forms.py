from django import forms
from .models import Finance_Report
class Finance_TotalForm(forms.ModelForm):

    class Meta:
        model = Finance_Report
        fields = ('salary', 'investment', 'total',"payment")  