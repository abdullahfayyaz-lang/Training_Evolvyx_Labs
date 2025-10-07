from django.contrib import admin
from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about,name='about'),
    path('services/', views.services,name='services'),
    path('contact/', views.contact,name='contact'),
    path('contact_view/', views.contact_view, name='contact_view'),
    path('customer_view/', views.customer_view, name='customer'),
    path('student_view/', views.student_view, name='student'),
    path('student/edit/<int:id>/', views.edit_student, name='edit_student'),

]