
from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('teachers', views.teachers, name='teachers'),
    path('courses', views.courses, name='courses'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contacts'),
    path('event', views.event, name='event'),
    path('news', views.news, name='news'),
    path('all_course', views.all_course, name='all_course'),
    path('mobileapp', views.mobileapp, name='mobileapp'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup')


]
