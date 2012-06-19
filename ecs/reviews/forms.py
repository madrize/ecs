from django import forms

RATING_CHOICES = [(5,5),(4,4),(3,3),(2,2),(1,1)]

class ReviewForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    rating = forms.ChoiceField(choices=RATING_CHOICES)
