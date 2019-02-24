from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
	if request.method == "POST":
		HttpResponse("success!")
	return render(request,"front.html")