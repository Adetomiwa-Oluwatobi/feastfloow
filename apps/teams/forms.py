from django import forms
from .models import Team

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Team Name'}),
            'description': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your team'}),
        }


class InviteForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Invite team member via email'}))
