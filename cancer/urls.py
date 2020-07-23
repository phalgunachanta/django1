from django.urls import path
from cancer import views

urlpatterns = [
	path("index/",views.index,name="index"),
	path('home/',views.home,name="home"),
	path('contact/',views.contact,name="contact"),
	path('register/',views.register,name="register"),
	path('login/',views.login,name="login"),
	path('changepassword/',views.changepassword,name="changepassword"),
	path('showpatients/',views.showpatients,name="showpatients"),
]


