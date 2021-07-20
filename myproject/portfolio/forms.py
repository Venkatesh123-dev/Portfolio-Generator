from django.contrib.auth.forms import UserCreationForm

from django import forms
from .models import Portfolio, Feedback
from django.contrib.auth.models import User




class SignUpForm(UserCreationForm):


    user_name= forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
	

    class Meta:
        model = User
        fields = ('user_name','password1','password2','first_name','last_name')


class PortfolioForm(forms.ModelForm):
	main_bio = forms.CharField(widget = forms.Textarea)
	widgets = {
		'date_of_birth': forms.DateInput(attrs={'id': 'id_date_of_birth'})
	}
	class Meta:
		model = Portfolio
		exclude = ['user']

class FeedbackForm(forms.ModelForm):
	feedback_field = forms.CharField(widget = forms.Textarea)

	class Meta:
		model = Feedback
		exclude = ['user']