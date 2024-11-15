from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('register_user/', views.register_user, name='register_user'),
    path('login/',views.login,name='login'),
    path('register_doctor/',views.register_doctor,name='register_doctor'),
    path('about/',views.about,name='about'),

]