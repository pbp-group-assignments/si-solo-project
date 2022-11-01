from django import forms

class TempatKulinerForms(forms.Form):
    kuliner_title = forms.CharField(max_length=255)
    kuliner_description = forms.CharField(max_length=500)
    kuliner_highlight = forms.CharField(max_length=500)