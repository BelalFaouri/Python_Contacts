from django.conf.urls import url

from . import views

#your code is here
urlpatterns = [
	url('contacts/',views.contacts,name='index.html')


]
