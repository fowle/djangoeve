from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, authenticate, login

def index(request):
	return render(request, 'evedb/index.html')
	
def git(request):
	return render(request, 'evedb/git.html')
	
def logout_d(request):
	logout(request)
	return HttpResponseRedirect(reverse('evedb:index'))
	
def login_d(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
