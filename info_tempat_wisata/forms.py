from django import forms

class TempatWisataForms(forms.Form):
    wisata_title = forms.CharField(max_length=255)
    wisata_description = forms.CharField(max_length=500)
    wisata_highlight = forms.CharField(max_length=500)