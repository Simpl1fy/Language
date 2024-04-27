# language_prediction_app/forms.py
from django import forms

class LanguagePredictionForm(forms.Form):
    text = forms.CharField(label='Enter text', widget=forms.Textarea)
