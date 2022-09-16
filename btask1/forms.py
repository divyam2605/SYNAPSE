from django import forms


class APIForm(forms.Form):
    Company = forms.CharField(max_length=100)
    About = forms.CharField(max_length=100)
