from django import forms

from cart.models import Cart


class CartForm(forms.ModelForm):
    quantity = forms.IntegerField()
    updated = forms.BooleanField(required=False,
                                 initial=False,
                                 widget=forms.HiddenInput)

    class Meta:
        model = Cart
        fields = ['quantity', 'updated']