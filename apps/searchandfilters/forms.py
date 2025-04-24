from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Search by name, role, or location'}))
    job_role = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Job Role'}))
    location = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Location'}))
    verified = forms.BooleanField(required=False)
    min_rating = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Minimum Rating'}))
    max_price_rate = forms.DecimalField(required=False, widget=forms.NumberInput(attrs={'placeholder': 'Maximum Price Rate'}))
