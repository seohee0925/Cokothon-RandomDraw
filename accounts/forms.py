from django import forms
from .models import Accounts
class accountForm(forms.ModelForm):
    # email = forms.CharField(max_length=100)
    # name = forms.CharField(max_length=100)
    # password = forms.CharField(max_length=100)
    # coin = forms.IntegerField()
    
    class Meta:
        model = Accounts
        # fields = '__all__'
        fields = ['email', 'name', 'password']
