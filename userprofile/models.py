from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create A User Profile Model
OCCUPATION 		= 	(('Imaam-khatib','Imaam-khatib'),
		 			('Muazzin','Muazzin'),
		 			('Accountant','Accountant'),
		  			('Actor','Actor'),
		  			('Doctor','Doctor'),
		  			('Teacher','Teacher'),
		  			('Writer','Writer'),
		  			('Farmer','Farmer'),
		  			('Engineer','Engineer'),
		  			('Lawyer','Lawyer'),
		  			('Business-person','Business-person'),
		  			('Journalist','Journalist'),
		  			('Banker','Banker'),
		  			('Student','Student'),
		  			('House-wife','House-wife'),
		  			('Govt-employee','Govt-employee'),
		  			('Private-company','Private-company'),
					('probashi','probashi'),
		  			('Others','Others'))

GENDER		 	= 	(('Male','Male'),
		  			('Female','Female'))

RELIGION		=	(('Islam','Islam'),
	     			('Christianity','Christianity'),
		 			('Buddhism','Buddhism'),
		 			('Hinduism','Hinduism'),
		 			('Judaism','Judaism'),
		 			('Sikhism','Sikhism'),
		 			('Zoroastrianism','Zoroastrianism'),
		 			('Others religion','Others religion'))

MARITAL_STATUS 	= 	(('Never married','Never married'),
		  			('Short divorced','Short divorced'),
		  			('Divorced','Divorced'),
		  			('Separated','Separated'),
		  			('Widow','Widow'),
		  			('Widower','Widower'))

class Profile(models.Model):
	user	                = models.OneToOneField(User, on_delete=models.CASCADE)
	following            	= models.ManyToManyField("self", related_name="followers",symmetrical=False,blank=True)	
	
	occupation				= models.CharField(null=True, blank=True, max_length=20,choices=OCCUPATION)
	education				= models.CharField(null=True, blank=True, max_length=100)
	birthday  				= models.DateField(null=True, blank=True)
	gender					= models.CharField(null=True, blank=True, max_length=6,choices=GENDER)
	height					= models.CharField(null=True, blank=True, max_length=10)
	weight					= models.CharField(null=True, blank=True, max_length=10)
	religion				= models.CharField(null=True, blank=True, max_length=20,choices=RELIGION)			
	marital_status			= models.CharField(null=True, blank=True, max_length=20,choices=MARITAL_STATUS)
	contact_no				= models.CharField(null=True, blank=True, max_length=11)
	present_address 		= models.TextField(null=True, blank=True)
	permanent_address		= models.TextField(null=True, blank=True)

	profile_bio          	= models.CharField(null=True, blank=True, max_length=500)
	homepage_link        	= models.CharField(null=True, blank=True, max_length=100)
	facebook_link        	= models.CharField(null=True, blank=True, max_length=100)
	instagram_link       	= models.CharField(null=True, blank=True, max_length=100) 
	linkedin_link        	= models.CharField(null=True, blank=True, max_length=100)

	profile_image        	= models.ImageField(null=True, blank=True, upload_to="profile_images/")
	view_count           	= models.IntegerField(default=1)
	date_modified        	= models.DateTimeField(User, auto_now=True)
	profile_status          = models.BooleanField(default=True) 
	

	def __str__(self):
		return self.user.username
	
	def percentofview(self):
		return self.view_count*0.001
	

# Create Profile When New User Signs Up
@receiver(post_save, sender=User)
def Create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()
		# Have the user follow themselves
		user_profile.following.set([instance.profile.id])
		user_profile.save()

#post_save.connect(create_profile, sender=User)


class Notification(models.Model):
    is_read 			= models.BooleanField(default=False)
    message 			= models.CharField(max_length=100)
    timestamp 			= models.DateTimeField(auto_now_add=True)
    user 				= models.ForeignKey(User, on_delete=models.CASCADE)
    
# class Whoprofileview(models.Model):
#     user 				= models.ForeignKey(User, on_delete=models.CASCADE)
#     view_user           = models.ManyToManyField()
#     timestamp 			= models.DateTimeField(auto_now_add=True)

class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.profile.user.username

class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.body