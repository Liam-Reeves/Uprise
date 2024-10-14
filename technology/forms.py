from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=200, required=True, widget=forms.TextInput(attrs = {'placeholder': "Name", }))
    email = forms.EmailField(max_length=200, required=True, widget=forms.EmailInput(attrs = {'placeholder': "Email",}))
    message = forms.CharField(max_length=1500, required = False, widget = forms.Textarea(attrs={ 'placeholder': 'Message' }))