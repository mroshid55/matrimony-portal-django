from django.db import models
from django.contrib.auth.models import User
from datetime import date,timedelta
# create ads model

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

BLOOD_GROUP 	= 	(('A+','A+'),
		  			('O+','O+'),
		  			('B+','B+'),
		  			('AB+','AB+'),
		  			('A-','A-'),
		  			('O-','O-'),
					('B-','B-'),
					('AB-','AB-'))


SKINCOLOR 		= 	(('Pale skin','Pale skin'),
		  			('Fair skin','Fair skin'),
		  			('Medium skin','Medium skin'),
		  			('Olive skin','Olive skin'),
		  			('Naturally brown skin','Naturally brown skin'),
		  			('Very dark brown skin','Very dark brown skin'))

class Advertisement(models.Model):
	user = models.ForeignKey(
		User, related_name="Advertisements", 
		on_delete=models.DO_NOTHING
		)
	post_title 				= models.CharField(max_length=100)
	frist_name 			    = models.CharField(max_length=50)
	last_name 			    = models.CharField(max_length=50)
	father_name             = models.CharField(max_length=50)
	father_profession       = models.CharField(max_length=50,choices=OCCUPATION)
	mother_name 			= models.CharField(max_length=50)
	mother_profession       = models.CharField(max_length=50,choices=OCCUPATION)
	birthday 				= models.DateField()
	gender                  = models.CharField(max_length=6,choices=GENDER)
	height 					= models.CharField(max_length=10)
	weight 					= models.CharField(max_length=10)
	blood_group 			= models.CharField(max_length=3,choices=BLOOD_GROUP)
	skin_color 				= models.CharField(max_length=20,choices=SKINCOLOR)
	religion      			= models.CharField(max_length=15,choices=RELIGION)
	marriage_status 		= models.CharField(max_length=17,choices=MARITAL_STATUS)
	education               = models.CharField(max_length=50)
	occupation              = models.CharField(max_length=15,choices=OCCUPATION)
	present_address 		= models.TextField(blank=True,null=True)
	permanent_address       = models.TextField(blank=True,null=True)
	Sister_brother_details  = models .TextField(blank=True,null=True)
	others 					= models.TextField(blank=True,null=True)
	likes 					= models.ManyToManyField(User, related_name="Advertisement_like", blank=True)
	created_at 				= models.DateTimeField(auto_now_add=True)


	# Keep track or count of likes
	def number_of_likes(self):
		return self.likes.count()



	def __str__(self):
		return(
			f"{self.user} "
			f"({self.created_at:%Y-%m-%d %H:%M}): "
			f"{self.post_title}..."
			)