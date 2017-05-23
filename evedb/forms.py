from django import forms
from .models import SSToken

class TokenForm(forms.ModelForm):
	class Meta:
		model = SSToken
		fields = ['token']
		labels = {'token': ''}
		
class GetImageForm(forms.ModelForm):
	image_id = forms.CharField(max_length=100)		