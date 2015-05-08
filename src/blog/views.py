from django.shortcuts import redirect, render, get_object_or_404
from django.core.urlresolvers import reverse
from django.utils import timezone

from blog import models
from blog import forms

# Create your views here.
def edit(request, slug):
	post = get_object_or_404(models.Post, slug=slug)
	current_post_status = post.status
	form = forms.PostEdit(instance=post)

	if request.POST:
		form = forms.PostEdit(request.POST, instance=post)
		if form.is_valid():
			updated_post = form.save(commit=False)

			if current_post_status == 1 and updated_post.status == 2:
				updated_post.publish = timezone.now()
			updated_post.save()
			return redirect('dashboard')			

	template = 'edit_post.html'
	context = {
		'form': form,
	}

	return render(request, template, context)