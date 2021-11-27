from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'index.html',{})


def contact(request):

	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		message = request.POST['message']
		return render(request,'contact.html',{'email': email})

	else:

		return render(request,'contact.html',{})


def project(request):
	return render(request,'portfolio.html',{})