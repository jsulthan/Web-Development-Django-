from django.urls import path, include
from. import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('km_page/', views.kmpage, name='km_page'),
    path('beings_page/', views.beingspage, name='beings_page'),
    path('medical_page/', views.medicalpage, name='medical_page'),
    path('genetics_page/', views.geneticspage, name='genetics_page'),
    path('content_page/', views.contentpage, name='content_page'),
    path('converse/', views.converse, name='converse'),
    path('company/', views.company, name='company'),
    path('about_us/', views.aboutus, name='about_us'),
    path('foundations/', views.foundations, name='foundations'),
    path('contact/', views.contact, name='contact'),
    path('careers/', views.careers, name='careers'),
    path('careers_form/', views.careersform, name='careers_form'),
    path('complete/', views.complete, name='complete'),

    path('accounts/', include("django.contrib.auth.urls")),
    path('register/', views.register, name='register'),
    path('oauth/', include("social_django.urls")),

    #path('blog/', views.blog, name="blog"),
    #path('room/<str:pk>/', views.room, name="room"),
    #path('create-room/', views.createRoom, name="create-room"),
    #path('edit-room/<str:pk>/', views.updatedRoom, name="edit-room"),
    #path('delete-room/<str:pk>/', views.deleteRoom, name="delete-room"),
]