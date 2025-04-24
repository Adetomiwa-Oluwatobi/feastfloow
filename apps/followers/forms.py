from django import forms

class ConnectionRequestForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a message (optional)'}), required=False)
