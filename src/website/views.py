from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth import logout as logout_user
from django.contrib.auth import login as login_user
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.contrib import messages
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from blog import models as blog_models
from website import models

# Create your views here.

def home(request):

	page = int(request.GET.get('page', 0))

	offset = page * 5
	limit = (page + 1) * 5

	print offset, limit

	posts = blog_models.Post.objects.filter(status=2).order_by('-publish')[offset:limit]

	template = 'index.html'
	context = {
		'posts': posts,
		'page': page,
	}

	return render(request, template, context)

def about(request):

	template = 'about.html'
	context = {}

	return render(request, template, context)

def page(request, page):

	page = get_object_or_404(models.Page, slug=page)

	template = 'page.html'
	context = {
		'page': page,
	}

	return render(request, template, context)

@login_required
def dashboard(request):

	latest_blog_posts = blog_models.Post.objects.all().order_by('-created')[:5]
	website_pages = models.Page.objects.all().order_by('-title')

	template = 'dashboard.html'
	context = {
		'latest_blog_posts': latest_blog_posts,
		'website_pages': website_pages,
	}

	return render(request, template, context)

# Authentication Views

def login(request):
	if request.user.is_authenticated():
		messages.info(request, 'You are already logged in.')
		return redirect(reverse('monitor_dashboard'))

	if request.POST:
		user = request.POST.get('user_name')
		pawd = request.POST.get('user_pass')

		user = authenticate(username=user, password=pawd)

		if user is not None:
			if user.is_active:
				login_user(request, user)
				messages.info(request, 'Login successful.')
				if request.GET.get('next'):
					return redirect(request.GET.get('next'))
				else:
					return redirect(reverse('home'))
			else:
				messages.add_message(request, messages.ERROR, 'User account is not active.')
		else:
			messages.add_message(request, messages.ERROR, 'Account not found with those details.')

	context = {}
	template = 'login.html'

	return render(request, template, context)

@login_required
def logout(request):
	messages.info(request, 'You have been logged out.')
	logout_user(request)
	return redirect(reverse('home'))

