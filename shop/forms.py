from django import forms

class ContactForm(forms.Form):
    """
    A form for users to contact the site administrators.

    This form includes fields for the user's email address, the subject of the message,
    and the message itself.

    Attributes:
    :param name: The name of the email address
    :type email: str
    :param subject: The subject of the message
    :type subject: str
    :param message: The content in the message
    :type message: str
    """
    email = forms.EmailField(required=True, label='Your email address')
    subject = forms.CharField(max_length=100, label='Subject')
    message = forms.CharField(widget=forms.Textarea, label='Message')
