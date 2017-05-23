from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

from .models import SSToken
from .forms import TokenForm, GetImageForm

def index(request):
	return render(request, 'evedb/index.html')
	
@login_required	
def git(request):
	return render(request, 'evedb/git.html')

@login_required
def ss(request):
	return render(request, 'evedb/ss.html')
	
def logout_d(request):
	logout(request)
	return HttpResponseRedirect(reverse('evedb:index'))
	
@login_required
def new_token(request):
	if request.method != 'POST':
		form = TokenForm()
	else:
		form = TokenForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('evedb:ss'))
			
	context = {'form': form}
	return render(request, 'evedb/new_token.html', context)
	
@login_required
def get_image(request):
	if request.method != 'POST':
		form = GetImageForm()
	else:
		form = GetImageForm(request.POST)
		if form.is_valid():
			image_id = request.POST['image_id']
			return HttpResponseRedirect(reverse('evedb:ss'))
			
	context = {'form': form}
	return render(request, 'evedb/ss.html', context)