from django.conf.urls import url,include

from . import views
from django.views.generic import DetailView
from .models import LatestUpdates



urlpatterns = [
	
	
	 url(r'^$',views.index,name='index'),
	 url(r'^notice/(?P<pk>\d+)$',DetailView.as_view(model=LatestUpdates,template_name='base/update_detail.html')),
	 url(r'^accounts/',include('django.contrib.auth.urls')),
	 url(r'^accounts/profile/$',views.profile,name="profile"),
	 url(r'^student/(?P<pk>\d+)$', views.UserProfileDetailView.as_view(), name='student-detail'),                        
	
	url(r'^studentlist/(?P<type>[-\w+]+)/(?P<year>[-\w+]+)$', views.UserProfileListView.as_view(), name='student'),
	url(r'^accounts/profile/feedback$',views.FeedbackListView.as_view(),name="feedback"),
	url(r'^FeedbackDetail/create$', views.FeedbackCreateView.as_view(), name='create-feedback-detail'),

	url(r'^coures/$', views.Courses, name='courses'),
	url(r'^courselist/(?P<type>[-\w+]+)/(?P<year>[-\w+]+)$', views.CourseListView.as_view(), name='course-list'),
	url(r'^course/(?P<pk>\d+)$', views.CourseDetailView.as_view(), name='course-detail'),
	url(r'^tutorial/(?P<pk>\d+)/create/$', views.TutorialCreateView.as_view(), name='create-tutorial'),
	url(r'^lecnotes/(?P<pk>\d+)/create/$', views.LectureNotesCreateView.as_view(), name='create-lec-notes'),	
	url(r'^labassig/(?P<pk>\d+)/create/$', views.LabAssigCreateView.as_view(), name='create-lab-assig'),		
		
	url(r'^AcademicDetail/create$', views.AcademicDetailCreateView.as_view(), name='create-academic-detail'),
	url(r'^research/create$', views.ResearchCreateView.as_view(), name='create-research-detail'),
	url(r'^projects/create$', views.ProjectCreateView.as_view(), name='create-projects'),	 
	url(r'^experience/create$', views.ExperienceCreateView.as_view(), name='create-exp'),
	url(r'^accomp/create$', views.AccomplishmentsCreateView.as_view(), name='create-accomp'),	 
	url(r'^skill/create$', views.SkillsCreateView.as_view(), name='create-skill'),
	url(r'^contact/create$', views.ContactCreateView.as_view(), name='create-contact'),
			 

	url(r'^AcademicDetail/update/(?P<pk>\d+)$', views.AcademicDetailUpdate.as_view(), name='update'),
	url(r'^projects/update/(?P<pk>\d+)$', views.ProjectsUpdate.as_view(), name='update-projects'),
	url(r'^experience/update/(?P<pk>\d+)$', views.ExperienceUpdate.as_view(), name='update-exp'),
	url(r'^accomp/update/(?P<pk>\d+)$', views.AccomplishmentsUpdate.as_view(), name='update-accomp'),
	url(r'^skill/update/(?P<pk>\d+)$', views.SkillsUpdate.as_view(), name='update-skill'),
	url(r'^contact/update/(?P<pk>\d+)$', views.ContactUpdate.as_view(), name='update-contact'),
	url(r'^userprofile/update/(?P<pk>\d+)$', views.UserProfileUpdate.as_view(), name='update-profile'),
	

	url(r'^AcademicDetai/delete/(?P<pk>\d+)$', views.AcademicDetailDelete.as_view(), name='delete'),
	url(r'^projects/delete/(?P<pk>\d+)$', views.ProjectsDelete.as_view(), name='delete-projects'),
	url(r'^experience/delete/(?P<pk>\d+)$', views.ExperienceDelete.as_view(), name='delete-exp'),
	url(r'^accomp/delete/(?P<pk>\d+)$', views.AccomplishmentsDelete.as_view(), name='delete-accomp'),
	url(r'^skill/delete/(?P<pk>\d+)$', views.SkillsDelete.as_view(), name='delete-skill'),
	url(r'^contact/delete/(?P<pk>\d+)$', views.ContactDelete.as_view(), name='delete-contact'),

]
