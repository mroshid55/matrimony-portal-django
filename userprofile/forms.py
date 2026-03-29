from django import forms
from .models import Profile,ChatMessage

# Profile Extras Form
class ProfilePicForm(forms.ModelForm):
	profile_image = forms.ImageField(label="Profile Picture")
	profile_bio = forms.CharField(label="Profile Bio", widget=forms.Textarea(attrs={'class':'form-control', 'placeholder':'Profile Bio'}))
	homepage_link = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Website Link'}))
	facebook_link =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Facebook Link'}))
	instagram_link = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Instagram Link'}))
	linkedin_link =  forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Linkedin Link'}))
	
	class Meta:
		model = Profile
		fields = ('occupation',
		        'education',
	            'birthday',
		        'gender',
                'height',
		        'weight',
                'religion',
                'marital_status',
                'contact_no',
                'present_address',
                'permanent_address',
                'profile_image', 
                'profile_bio', 
                'homepage_link', 
                'facebook_link', 
                'instagram_link',
                'linkedin_link', )
                
class ChatMessageForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"class":"forms", "rows":3, "placeholder": "Type message here"}))
    class Meta:
        model = ChatMessage
        fields = ["body",]