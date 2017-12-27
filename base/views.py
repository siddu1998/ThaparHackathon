from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .forms import *
from django import forms
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.db.models import Count
from datetime import datetime
from uclassify import uclassify


# Create your views here.

class FeedbackListView(LoginRequiredMixin,generic.ListView):
	model=Feedback
	def get_context_data(self, **kwargs):
		context = super(FeedbackListView, self).get_context_data(**kwargs)
		context['q1']=list(Feedback.objects.filter(Teacher=self.request.user).values('Presents_material_in_a_variety_of_ways').annotate(the_count=Count('Presents_material_in_a_variety_of_ways')))
		context['q2']=list(Feedback.objects.filter(Teacher=self.request.user).values('Planned_to_communicate_why_learning_this_is_important').annotate(the_count=Count('Planned_to_communicate_why_learning_this_is_important')))
		context['q3']=list(Feedback.objects.filter(Teacher=self.request.user).values('The_information_was_presented_logically').annotate(the_count=Count('The_information_was_presented_logically')))
		context['q4']=list(Feedback.objects.filter(Teacher=self.request.user).values('How_is_the_pace_of_the_class').annotate(the_count=Count('How_is_the_pace_of_the_class')))
		context['q5']=list(Feedback.objects.filter(Teacher=self.request.user).values('Were_notes_efficient_for_after_learning').annotate(the_count=Count('Were_notes_efficient_for_after_learning')))
		
		context['q1_today']=list(Feedback.objects.filter(Teacher=self.request.user,date=datetime.now()).values('Presents_material_in_a_variety_of_ways').annotate(the_count=Count('Presents_material_in_a_variety_of_ways')))
		context['q2_today']=list(Feedback.objects.filter(Teacher=self.request.user,date=datetime.now()).values('Planned_to_communicate_why_learning_this_is_important').annotate(the_count=Count('Presents_material_in_a_variety_of_ways')))
		context['q4_today']=list(Feedback.objects.filter(Teacher=self.request.user,date=datetime.now()).values('How_is_the_pace_of_the_class').annotate(the_count=Count('How_is_the_pace_of_the_class')))
		context['q5_today']=list(Feedback.objects.filter(Teacher=self.request.user,date=datetime.now()).values('Were_notes_efficient_for_after_learning').annotate(the_count=Count('Were_notes_efficient_for_after_learning')))

		
		return context

	def get_queryset(self):
		queryset=Feedback.objects.filter(Teacher=self.request.user)
		return queryset

class FeedbackCreateView(LoginRequiredMixin,generic.CreateView):
	model=Feedback
	form_class= FeedbackForm
	template_name='base/detailcreate_form.html'

	def get_context_data(self,**kwargs):
		context=super(FeedbackCreateView,self).get_context_data(**kwargs)
		ls=list(self.request.user.groups.values_list('name',flat=True))
		context['Teacher']=User.objects.filter(groups__name='COE20')

		return context

	def form_valid(self,form):
		feedback=form.save(commit=False)
		feedback.Student=User.objects.get(username=self.request.user)
		a = uclassify()
		a.setWriteApiKey('-----GET YOUR OWN WRITE KEY-----')
		a.setReadApiKey('-----GET YOUR OWN READ KEY-----')
		#a.create("GorB") #Creates Classifier named "ManorWoman"
		#a.addClass(["g","b"],"gorb") #Adds two class named "man" and "woman" to the classifier "ManorWoman"
		a.train(["Boring Bad","Late Slow","Too Fast","Dull BC MC BKL MKL Ganda Wost Worse Sleep Din't  Not Can't"],"b","GorB")
		a.train(["Nice Well Good Happy Great Amazing Wonderful Awsome MindBlowing Crazy "],"g","GorB")        
		d = a.classify([feedback.comments],"GorB")
		
		feedback.ifactor=int(float(ls1+0.1)*10)
        
		feedback.save()
		return redirect('/accounts/profile')
	def get_form_kwargs(self):
		kwargs=super(FeedbackCreateView,self).get_form_kwargs()
		kwargs.update({'user':self.request.user})
		return kwargs
	
		

def index(request):
	update_list=LatestUpdates.objects.all().order_by("-date")[:10]
	context={'uList':update_list}
	return render(request,'base/index.html',context)

@login_required
def profile(request):
	context={'count_paper':list(Research_Paper.objects.filter(author=request.user).order_by('year').values('year').annotate(the_count=Count('year')))}
	return render(request,'registration/profile.html',context)

class UserProfileListView(generic.ListView):
	model=UserProfile
	def get_context_data(self, **kwargs):
		context = super(UserProfileListView, self).get_context_data(**kwargs)
		
		id_list = UserProfile.objects.all()
		record = []
		for item in id_list:
			data = {
			'pk' : item.pk,
			'count' : Skills.objects.filter(user=item).count(),
			'project':Projects.objects.filter(user=item).count()
			}
			record.append(data)
		context['count'] = record
		return context
		
	def get_queryset(self):
		queryset=UserProfile.objects.filter(user_type__exact=self.kwargs['type'] , user_year__exact=self.kwargs['year'])

		query=self.request.GET.get('q')
		if query:

			filter_arg=Q(skills__skill_name__icontains=query)| Q(first_name__icontains=query)
			try:
				filter_arg |= Q(current_cgpa__gte=float(query))
			except ValueError:
				pass

			queryset=queryset.filter(filter_arg).distinct()
			return queryset
		
		return UserProfile.objects.filter(user_type__exact=self.kwargs['type'] , user_year__exact=self.kwargs['year'])


class UserProfileDetailView(generic.DetailView):
	model=UserProfile
	
	def get_context_data(self, **kwargs):
		context = super(UserProfileDetailView, self).get_context_data(**kwargs)
		context['count_paper']=list(Research_Paper.objects.filter(author=self.kwargs['pk']).order_by('year').values('year').annotate(the_count=Count('year')))
		context['group_name']=list(self.request.user.groups.values_list('name',flat=True))
		return context
	
class AcademicDetailCreateView(LoginRequiredMixin,generic.CreateView):
	model=AcademicDetail
	form_class= AcademicDetailForm
	template_name='base/detailcreate_form.html'

	def form_valid(self,form):
		academicdetail=form.save(commit=False)
		academicdetail.user=UserProfile.objects.get(user=self.request.user)
		academicdetail.save()
		return redirect('/accounts/profile')
class ResearchCreateView(LoginRequiredMixin,generic.CreateView):
	model=Research_Paper
	form_class= ResearchDetailForm
	template_name='base/detailcreate_form.html'

	def form_valid(self,form):
		researchdetail=form.save(commit=False)
		
		researchdetail.save()
		return redirect('/accounts/profile')


class AcademicDetailUpdate(LoginRequiredMixin,generic.UpdateView):
		model=AcademicDetail
		template_name='base/detailupdate_form.html'
		fields = ["desciption","institute",
		"percentage",
		"entering",
		"leaving",
	]
		


class AcademicDetailDelete(LoginRequiredMixin,generic.DeleteView):
    
    model=AcademicDetail
    success_url=reverse_lazy('profile')
    template_name='base/detaildelete_form.html'


class ProjectCreateView(LoginRequiredMixin,generic.CreateView):
	model=Projects
	form_class= ProjectsForm
	template_name='base/detailcreate_form.html'

	def form_valid(self,form):
		projects=form.save(commit=False)
		projects.user=UserProfile.objects.get(user=self.request.user)
		projects.save()
		return redirect('/accounts/profile')


class ProjectsUpdate(LoginRequiredMixin,generic.UpdateView):
		model=Projects
		template_name='base/detailupdate_form.html'
		fields = ["title","desciption","link","start_date","end_date",]
		


class ProjectsDelete(LoginRequiredMixin,generic.DeleteView):
    
    model=Projects
    success_url=reverse_lazy('profile')
    template_name='base/detaildelete_form.html'

class ExperienceCreateView(LoginRequiredMixin,generic.CreateView):
	model=Experience
	form_class= ExperienceForm
	template_name='base/detailcreate_form.html'

	def form_valid(self,form):
		experience=form.save(commit=False)
		experience.user=UserProfile.objects.get(user=self.request.user)
		experience.save()
		return redirect('/accounts/profile')


class ExperienceUpdate(LoginRequiredMixin,generic.UpdateView):
		model=Experience
		fields = [
		"title",
		"desciption",
		"organisation",
		
		"start_date",
		"end_date",
	]
		template_name='base/detailupdate_form.html'


class ExperienceDelete(LoginRequiredMixin,generic.DeleteView):
    
    model=Experience
    success_url=reverse_lazy('profile')
    template_name='base/detaildelete_form.html'

class AccomplishmentsCreateView(LoginRequiredMixin,generic.CreateView):
	model=Accomplishments
	form_class= AccomplishmentsForm
	template_name='base/detailcreate_form.html'

	def form_valid(self,form):
		accomplishments=form.save(commit=False)
		accomplishments.user=UserProfile.objects.get(user=self.request.user)
		accomplishments.save()
		return redirect('/accounts/profile')

class AccomplishmentsUpdate(LoginRequiredMixin,generic.UpdateView):
		model=Accomplishments
		fields = [
		"title",
		"desciption",
		
	]
		template_name='base/detailupdate_form.html'

class AccomplishmentsDelete(LoginRequiredMixin,generic.DeleteView):
    
    model=Accomplishments
    success_url=reverse_lazy('profile')
    template_name='base/detaildelete_form.html'

class SkillsCreateView(LoginRequiredMixin,generic.CreateView):
	model=Skills
	form_class= SkillsForm
	template_name='base/detailcreate_form.html'

	def form_valid(self,form):
		skills=form.save(commit=False)
		skills.user=UserProfile.objects.get(user=self.request.user)
		skills.save()
		return redirect('/accounts/profile')

class SkillsUpdate(LoginRequiredMixin,generic.UpdateView):
		model=Skills
		fields = [
		"skill_name",
		
		
	]
		template_name='base/detailupdate_form.html'

class SkillsDelete(LoginRequiredMixin,generic.DeleteView):
    
    model=Skills
    success_url=reverse_lazy('profile')
    template_name='base/detaildelete_form.html'

class ContactCreateView(LoginRequiredMixin,generic.CreateView):
	model=Contact
	form_class= ContactForm
	template_name='base/detailcreate_form.html'

	def form_valid(self,form):
		contact=form.save(commit=False)
		contact.user=UserProfile.objects.get(user=self.request.user)
		contact.save()
		return redirect('/accounts/profile')

class ContactUpdate(LoginRequiredMixin,generic.UpdateView):
		model=Contact
		fields = [
		"email_id","phone"
		
		
	]
		template_name='base/detailupdate_form.html'

class ContactDelete(LoginRequiredMixin,generic.DeleteView):
    
    model=Contact
    success_url=reverse_lazy('profile')
    template_name='base/detaildelete_form.html'



class UserProfileUpdate(LoginRequiredMixin,generic.UpdateView):
	
		model=UserProfile
		success_url=reverse_lazy('profile')
		fields = ["first_name","last_name","desciption","profile_image","user_year"]
		template_name='base/userprofileupdate_form.html'

def Courses(request):
	return render(request,'base/course.html')
class CourseListView(generic.ListView):
	model=Course
	def get_queryset(self):
		return Course.objects.filter(user_type__exact=self.kwargs['type'] , course_year__exact=self.kwargs['year'])

class CourseDetailView(generic.DetailView):
	model=Course
	
		
class TutorialCreateView(LoginRequiredMixin,generic.CreateView):
	model=Tutorial
	form_class= TutorialForm
	template_name='base/corsemat_create_form.html'
	

	def get_context_data(self, **kwargs):
		context = super(TutorialCreateView, self).get_context_data(**kwargs)
		context['sub_code'] = get_object_or_404(Course, pk = self.kwargs['pk'])
		
		return context

	def form_valid(self,form):
		tutorial=form.save(commit=False)
		form.instance.sub_code=get_object_or_404(Course, pk = self.kwargs['pk'])
		return super(TutorialCreateView, self).form_valid(form)
class LectureNotesCreateView(LoginRequiredMixin,generic.CreateView):
	model=Lecture_notes
	form_class=Lecture_notesForm
	template_name='base/corsemat_create_form.html'
	

	def get_context_data(self, **kwargs):
		context = super(LectureNotesCreateView, self).get_context_data(**kwargs)
		context['sub_code'] = get_object_or_404(Course, pk = self.kwargs['pk'])
		
		return context

	def form_valid(self,form):
		lecture_notes=form.save(commit=False)
		form.instance.sub_code=get_object_or_404(Course, pk = self.kwargs['pk'])
		return super(LectureNotesCreateView, self).form_valid(form)
class LabAssigCreateView(LoginRequiredMixin,generic.CreateView):
	model=Lab_Assignment
	form_class=Lab_AssignmentForm
	template_name='base/corsemat_create_form.html'
	

	def get_context_data(self, **kwargs):
		context = super(LabAssigCreateView, self).get_context_data(**kwargs)
		context['sub_code'] = get_object_or_404(Course, pk = self.kwargs['pk'])
		
		return context

	def form_valid(self,form):
		lab_assignment=form.save(commit=False)
		form.instance.sub_code=get_object_or_404(Course, pk = self.kwargs['pk'])
		return super(LabAssigCreateView, self).form_valid(form)
	
		

