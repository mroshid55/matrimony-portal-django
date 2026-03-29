from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from advertisement.models import Advertisement
from crispy_forms.helper import FormHelper

class RegisterForm(UserCreationForm):
	email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)

		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = None

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = None

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = None

class DateInput(forms.DateInput):
    input_type = 'date'
class AdvertisementForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_show_labels = False
	post_title = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'একটি "অবিবাহিত" পাত্রের জন্য পাত্রী চাই'}))
	frist_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'নামের প্রথম অংশ'}))
	last_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'নামের শেষ অংশ'}))
	father_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'বাবার নাম'}))
	mother_name = forms.CharField(label="", max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'মায়ের নাম'}))
	birthday = forms.DateField(widget=DateInput)
	present_address  = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '',"rows": 2, "cols": 20}), max_length=100)
	permanent_address  = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '',"rows": 2, "cols": 20}), max_length=100)
	Sister_brother_details  = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '',"rows": 2, "cols": 20}), max_length=100)
	others  = forms.CharField(widget=forms.Textarea(attrs={'placeholder': '',"rows": 2, "cols": 20}), max_length=100)
	class Meta:
		model = Advertisement
		exclude = ("user", "likes","created_at",)