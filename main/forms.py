from django import forms
from .models import Capsule, picked_capsule

class CapsuleCreateForm(forms.ModelForm):
    class Meta:
        model = Capsule
        fields = ['content', 'picture', 'destination', 'open_date']

class pickedcapsuleForm(forms.ModelForm):
    class Meta:
        model = picked_capsule
        field = ['account_info_email',
    'info_write_date',
    'info_open_date',
    'info_content',
    'info_picture']