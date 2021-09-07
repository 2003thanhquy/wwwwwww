from django.shortcuts import render
from  django.http import HttpResponse

# Create your views here.



def home_view(request,*args , **kwargs):
	#return HttpResponse('<h1>helloword</h1>')
	return render (request , 'home.html',{})

def about_view(request,*args , **kwargs):
	about ={
	'my_about' : 'thanh quy 111',
	'my_list': [1,22,3,4] ,
	'mt':''
	}
	return render (request , 'about.html',about)	