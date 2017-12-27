from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.urls import reverse
from datetime import datetime

# Create your models here.
class LatestUpdates(models.Model):
	heading=models.CharField(max_length=50)
	text=models.TextField()
	PRIORITY_CHOICES=(('imp','Very Important'),('reg','Regular'))
	
	priority=models.CharField(max_length=3,choices=PRIORITY_CHOICES)

	date=models.DateTimeField(null=True) 	
	

	def __str__(self):
		return str(self.heading)

from django.core.validators import MaxValueValidator, MinValueValidator
	
class UserProfile(models.Model):
	user=models.OneToOneField(User)
	first_name=models.CharField(max_length=100,default='')
	last_name=models.CharField(max_length=100,default='')
	desciption=models.CharField(max_length=500,default='')
	USER_TYPE_CHOICES=(('btec','B.TECH'),('mtec','M.TECH'),('tea','teacher'),('rst','Reaserch Student'))
	profile_image=models.FileField(null=True,blank=True)
	user_type=models.CharField(max_length=4,choices=USER_TYPE_CHOICES)
	USER_YEAR_CHOICES=(('1st','1st Year Student'),('2nd','2nd Year Student'),('3rd','Third Year Student'),('4th','4th Year Student'),('phd','PHD'),('fac','Faculty'))
	user_year=models.CharField(max_length=3,choices=USER_YEAR_CHOICES,default='1st')
	current_cgpa=models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(10)],null=True)
	

	def __str__(self):
		return str(self.user.username)
	
	def get_absolute_url(self):
		return reverse('student-detail',args=[str(self.id)])

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile=UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

class AcademicDetail(models.Model):
	user=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
	
	desciption=models.TextField(null=True)
	institute=models.TextField(null=True)
	
	percentage=models.TextField(null=True,blank=True)
	entering=models.DateField(null=True)
	leaving=models.DateField(null=True)

	def __str__(self):
		return str(self.user)
	def get_absolute_url(self):
		return reverse('profile')

class Projects(models.Model):
	user=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
	title=models.TextField()
	desciption=models.TextField(null=True)
	link=models.TextField(null=True,blank=True)
	
	
	start_date=models.DateField(null=True)
	end_date=models.DateField(null=True)

	def __str__(self):
		return str(self.user)
	def get_absolute_url(self):
		return reverse('profile')

class Experience(models.Model):
	user=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
	title=models.TextField()
	desciption=models.TextField(null=True)
	organisation=models.TextField()
	
	
	start_date=models.DateField(null=True)
	end_date=models.DateField(null=True)

	def __str__(self):
		return str(self.user)
	def get_absolute_url(self):
		return reverse('profile')

class Accomplishments(models.Model):
	user=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
	title=models.TextField()
	desciption=models.TextField(null=True,blank=True)
	
	
	
	def __str__(self):
		return str(self.user)
	def get_absolute_url(self):
		return reverse('profile')

class Skills(models.Model):
	user=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
	skill_name=models.TextField()

	def __str__(self):
		return str(self.user)
	def get_absolute_url(self):
		return reverse('profile')
class Contact(models.Model):
	user=models.ForeignKey(UserProfile,on_delete=models.SET_NULL,null=True)
	phone=models.PositiveIntegerField(blank=True)
	email_id=models.EmailField()

	def __str__(self):
		return str(self.user)

	def get_absolute_url(self):
		return reverse('profile')

class Course(models.Model):
	sub_code=models.CharField(max_length=50)
	sub_name=models.CharField(max_length=100)
	syllabus=models.TextField()
	COURSE_TYPE_CHOICES=(('btec','B.TECH'),('mtec','M.TECH'),('tea','teacher'),('rst','Reaserch Student'))
	user_type=models.CharField(max_length=4,choices=COURSE_TYPE_CHOICES)
	COURSE_YEAR_CHOICES=(('1st','1st Year Student'),('2nd','2nd Year Student'),('3rd','Third Year Student'),('4th','4th Year Student'))
	course_year=models.CharField(max_length=3,choices=COURSE_YEAR_CHOICES,default='1st')
	corse_cord=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)

	def __str__(self):
		return str(self.sub_code)
	def get_absolute_url(self):
		return reverse('course-detail',args=[str(self.id)])

class Tutorial(models.Model):
	sub_code=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
	
	tut_number=models.CharField(max_length=100)
	date=models.DateField()
	tut_file=models.FileField()
	def __str__(self):
		return str(self.sub_code)
	def get_absolute_url(self):
		return reverse('course-detail',args=[str(self.sub_code.id)])


class Lecture_notes(models.Model):
	sub_code=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
	
	ppt_number=models.CharField(max_length=100)
	date=models.DateField()
	ppt_file=models.FileField()
	def __str__(self):
		return str(self.sub_code)
	def get_absolute_url(self):
		return reverse('course-detail',args=[str(self.sub_code.id)])

class Lab_Assignment(models.Model):
	sub_code=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
	
	assig_number=models.CharField(max_length=100)
	date=models.DateField()
	assig_file=models.FileField()
	def __str__(self):
		return str(self.sub_code)
	def get_absolute_url(self):
		return reverse('course-detail',args=[str(self.sub_code.id)])

class Research_Paper(models.Model):
	author = models.ManyToManyField(User, limit_choices_to={'groups__name':"Faculty"})
	title=models.CharField(max_length=500)
	description=models.TextField()
	year=models.CharField(max_length=4)

	impact_factor=models.FloatField(validators = [MinValueValidator(0), MaxValueValidator(10)],null=True)
	link=models.TextField(null=True,blank=True)
	def __str__(self):
		return str(self.title)	

class Feedback(models.Model):
	q1_CHOICES=(('Yes','Yes'),('No','No'),('Sometimes','Sometimes'),('NA','NA'))
	q2_CHOICES=(('Fast','Fast'),('Perfect','Perfect'),('Slow','Slow'))
	Student=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name="feed_stu")
	Teacher=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,limit_choices_to={'groups__name':"Faculty"})
	Presents_material_in_a_variety_of_ways=models.CharField(max_length=10,choices=q1_CHOICES,default='D')
	Planned_to_communicate_why_learning_this_is_important=models.CharField(max_length=10,choices=q1_CHOICES,default='D')
	The_information_was_presented_logically=models.CharField(max_length=10,choices=q1_CHOICES,default='D')
	How_is_the_pace_of_the_class=models.CharField(max_length=10,choices=q2_CHOICES,default='Slow')
	Were_notes_efficient_for_after_learning=models.CharField(max_length=10,choices=q1_CHOICES,default='NA')

	date=models.DateField(default=datetime.now,blank=True)
	comments=models.TextField(max_length=1000,blank=True)
	ifactor=models.IntegerField(default=6)
	def __str__(self):
		return str(self.Teacher)	
	
		




	
		
	





		
