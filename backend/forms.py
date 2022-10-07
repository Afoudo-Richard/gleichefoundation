from django import forms
from .models import *

class NewsBlogForm(forms.ModelForm):
	class Meta:
		model = NewsBlog
		fields = '__all__'


class ExecutiveForm(forms.ModelForm):
	class Meta:
		model = Executive
		fields = '__all__'

class VolunteerForm(forms.ModelForm):
	class Meta:
		model = Volunteer
		fields = '__all__'

class TestimonialForm(forms.ModelForm):
	class Meta:
		model = Testimonial
		fields = '__all__'

class SponsorForm(forms.ModelForm):
	class Meta:
		model = Sponsor
		fields = '__all__'

class CauseForm(forms.ModelForm):
	class Meta:
		model = Cause
		fields = '__all__'

class UpcomingEventForm(forms.ModelForm):
	class Meta:
		model = UpcomingEvent
		fields = '__all__'
		
class SlideForm(forms.ModelForm):
	class Meta:
		model = Slide
		fields = '__all__'

