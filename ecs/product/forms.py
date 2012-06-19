from django import forms

class AddToCartForm(forms.Form):
    """
    Form used to add an item to user's cart
    
    """
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'size':'2', 'value':'1', 'class':'quantity'}))
    product_slug = forms.CharField(widget=forms.HiddenInput())
    
    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super(AddToCartForm, self).__init__(*args, **kwargs)