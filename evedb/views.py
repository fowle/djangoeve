from django.shortcuts import render

def index(request):
	return render(request, 'evedb/index.html')
	
def git(request):
	return render(request, 'evedb/git.html')