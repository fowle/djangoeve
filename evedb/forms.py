from django import forms
from .models import SSToken

class TokenForm(forms.ModelForm):
	class Meta:
		model = SSToken
		fields = ['token']
		labels = {'token': ''}
		
class GetImageForm(forms.ModelForm):
	class Meta:
		image_id = forms.CharField(max_length=100)
		fields = ['image_id']
		labels = {'image_id': ''}		