from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db.models import Q



class AcademicDetailForm(forms.ModelForm):
    

	desciption=forms.CharField()
	institute=forms.CharField()
	percentage=forms.CharField()
	entering=forms.DateField(widget=forms.SelectDateWidget(years=range(1950,3000)))
	leaving=forms.DateField(widget=forms.SelectDateWidget(years=range(1950,3000)) 	)
	class Meta:
		model =  AcademicDetail
		fields = [
		"desciption",
		"institute",
		"percentage",
		"entering",
		"leaving",
	]
class ResearchDetailForm(forms.ModelForm):
    

	year=forms.CharField(label='Year : (please enter numeric four digit year only)')
	author = forms.CharField(widget=forms.Textarea, required=False)

	def clean_author(self):
		author_data = self.cleaned_data.get('author',None)
		author = []
        #here, a comma is used a delim, so it's not allowed in the tool name.
		for td in author_data.split(','): 
			t= User.objects.get_or_create(username=td)
			author.append(t)
			print(author)
			return author
	
	class Meta:
		model =  Research_Paper
		fields = [
		"author",
		"title",
		"description",
		"year",
		"impact_factor",
		"link"

	]

class ProjectsForm(forms.ModelForm):
    
	title=forms.CharField()
	desciption=forms.CharField()
	
	link=forms.CharField()
	start_date=forms.DateField(widget=forms.SelectDateWidget(years=range(1950,3000)))
	end_date=forms.DateField(widget=forms.SelectDateWidget(years=range(1950,3000)) 	)
	class Meta:
		model =  Projects
		fields = [
		"title",
		"desciption",
		"link",
		
		"start_date",
		"end_date",
	]

class ExperienceForm(forms.ModelForm):
    
	title=forms.CharField()
	desciption=forms.CharField()
	
	organisation=forms.CharField()
	start_date=forms.DateField(widget=forms.SelectDateWidget(years=range(1950,3000)))
	end_date=forms.DateField(widget=forms.SelectDateWidget(years=range(1950,3000)) 	)
	class Meta:
		model =  Experience
		fields = [
		"title",
		"desciption",
		"organisation",
		
		"start_date",
		"end_date",
	]

class AccomplishmentsForm(forms.ModelForm):
	helper = FormHelper()
	helper.form_tag = False
	title=forms.CharField()
	desciption=forms.CharField()
	
	
	class Meta:
		model =  Accomplishments
		fields = [
		"title",
		"desciption",
	]

class SkillsForm(forms.ModelForm):
	
	skill_name=forms.CharField()
	
	
	class Meta:
		model =Skills
		fields = [
		"skill_name",
		
	]

class ContactForm(forms.ModelForm):
	
	email_id=forms.CharField()
	phone=forms.CharField()
	
	
	class Meta:
		model =Contact
		fields = [
		"email_id","phone"
		
	]
	
class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('first_name' , 'last_name', "desciption", "profile_image","user_year")

class TutorialForm(forms.ModelForm):
	date=forms.DateField(widget=forms.SelectDateWidget(years=range(1950,3000)))
	class Meta:
		model=Tutorial
		fields=('tut_number','tut_file','date')

class Lecture_notesForm(forms.ModelForm):
	date=forms.DateField(widget=forms.SelectDateWidget(years=range(1950,3000)))
	class Meta:
		model=Lecture_notes
		fields=('ppt_number','ppt_file','date')
		
class Lab_AssignmentForm(forms.ModelForm):
	date=forms.DateField(widget=forms.SelectDateWidget(years=range(1950,3000)))
	class Meta:
		model=Lab_Assignment
		fields=('assig_number','assig_file','date')

class FeedbackForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		self.user=kwargs.pop('user')
		super(FeedbackForm, self).__init__(*args, **kwargs)
		ls=list(self.user.groups.values_list('name',flat=True))
		criteria1=Q(groups__name=ls[0])
		
		self.fields['Teacher'] = forms.ModelChoiceField(queryset=User.objects.filter(criteria1).exclude(groups__name="Student"))
	class Meta:
		model=Feedback
		title="Feedback"
		fields=['Teacher',
		'comments',
		'Presents_material_in_a_variety_of_ways',
		'Planned_to_communicate_why_learning_this_is_important',
		'The_information_was_presented_logically',
		'How_is_the_pace_of_the_class',
		'Were_notes_efficient_for_after_learning'
		]
		
		