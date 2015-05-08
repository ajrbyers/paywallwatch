from django import forms
from django.forms import ModelForm
from blog import models

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PostEdit(forms.ModelForm):
	body = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'height': '300px', 'styleWithSpan': 'false'}))

	class Meta:
		model = models.Post
		exclude = ('author', 'publish', 'created', 'modified', 'categories')