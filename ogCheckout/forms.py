from django import forms
from django_countries.fields import CountryField

payment_choice = (
    ('MT', 'MTN Mobile Money'),
    ('AT', 'Airtel Money'),
    ('AF', 'Africell Money'),
    ('I', 'Interswitch Cards'),
    ('VMU', 'Visa/MasterCard/UnionPay')
)
class CheckoutForm(forms.Form):
    f_name = forms.CharField()
    l_name = forms.CharField()
    country = CountryField(blank_label='(select country)')
    amount = forms.IntegerField()
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=payment_choice)