from django import forms


class ContactForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    pass
