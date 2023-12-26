from django import forms
from .models import Capsule

class CapsuleCreateForm(forms.ModelForm):
    class Meta:
        model = Capsule
        fields = '__all__'