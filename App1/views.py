from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

def home(request):
	return render(request,'homepage.html',{})

