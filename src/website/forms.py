from django import forms
from django.forms import ModelForm
from website import models

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class PageEdit(forms.ModelForm):
	body = forms.CharField(widget=SummernoteWidget(attrs={'width': '100%', 'height': '300px', 'styleWithSpan': 'false'}))

	class Meta:
		model = models.Page
		exclude = ('author', 'publish', 'created', 'modified', 'categories')