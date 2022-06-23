from django import forms
from .models import *

class NewsBlogForm(forms.ModelForm):
	class Meta:
		model = NewsBlog
		fields = '__all__'

