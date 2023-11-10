from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    sender_email = forms.EmailField(
        label="Email", required=True,
        widget=forms.EmailInput(attrs={
                "placeholder": "Email",
                }
        )
    )
    subject = forms.CharField(
        label="Subject", required=True,
        widget=forms.TextInput(attrs={
                "placeholder": "Subject",
                }
        )
    )
    message = forms.CharField(
        label="Message", required=True,
        widget=forms.Textarea(attrs={
                "placeholder": "Message",
                }
        )
    )

    class Meta:
        model = Contact
        fields = ["sender_email", "subject", "message"]