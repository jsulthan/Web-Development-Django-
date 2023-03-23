from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Document 

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('email', 'subject', 'document', )

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)