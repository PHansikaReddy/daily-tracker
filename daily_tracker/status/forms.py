from django import forms
from .models import DailyStatus

class DailyStatusForm(forms.ModelForm):
    class Meta:
        model = DailyStatus
        fields = ['day', 'question_name', 'link', 'document']
