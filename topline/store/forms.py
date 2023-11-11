from django import forms


class SiteNameForm(forms.Form):
    """
    
    """
    title_site = forms.CharField(max_length=100, help_text="Название", label='Новое название')

