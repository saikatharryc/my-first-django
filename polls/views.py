from django.http import HttpResponse

def index(request):
	return HttpResponse("Hi, You Hitted directly to The view of poll")