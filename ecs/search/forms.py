from django import forms
from product.models import Category

class SearchForm(forms.Form):
    search_key = forms.CharField()
    categories = forms.ModelChoiceField(queryset=Category.objects.all())