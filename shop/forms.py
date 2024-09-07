from django import forms

class ContactForm(forms.Form):
    email = forms.EmailField(required=True, label='Your email address')
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
