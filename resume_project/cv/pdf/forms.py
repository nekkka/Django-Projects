from django import forms 
from .models import Contact 

"""class ContactForm(forms.Form): 
    name = forms.CharField(max_length=100) 
    email = forms.EmailField() 
    message = forms.CharField(widget=forms.Textarea) """

class ContactForm(forms.ModelForm): 
    class Meta: 
        model = Contact 
        fields = ['name', 'email', 'message'] 