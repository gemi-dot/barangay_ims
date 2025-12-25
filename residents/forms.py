from django import forms
from .models import Resident

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = [
            'philhealth_number',
            'sss_gsis_number',
            'tin_number',
            'voters_id',
            'precinct_number',
        ]
        widgets = {
            'philhealth_number': forms.TextInput(attrs={'class': 'form-control'}),
            'sss_gsis_number': forms.TextInput(attrs={'class': 'form-control'}),
            'tin_number': forms.TextInput(attrs={'class': 'form-control'}),
            'voters_id': forms.TextInput(attrs={'class': 'form-control'}),
            'precinct_number': forms.TextInput(attrs={'class': 'form-control'}),
        }
