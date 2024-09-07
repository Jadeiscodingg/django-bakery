from django import forms

class ContactForm(forms.Form):
    """
    A form for users to contact the site administrators.

    This form includes fields for the user's email address, the subject of the message,
    and the message itself.

    Attributes:
    email (forms.EmailField): The user's email address.
    subject (forms.CharField): The subject of the message.
    message (forms.CharField): The message content.
    """
    email = forms.EmailField(required=True, label='Your email address')
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
