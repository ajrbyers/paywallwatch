from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from django.conf import settings

import datetime

class Category(models.Model):
	"""Category model."""
	title = models.CharField(_('title'), max_length=100)
	slug = models.SlugField(_('slug'), unique=True)

	class Meta:
		verbose_name = _('category')
		verbose_name_plural = _('categories')
		ordering = ('title',)

	def __unicode__(self):
		return u'%s' % self.title

class Post(models.Model):
	STATUS_CHOICES = (
		(1, _('Draft')),
		(2, _('Public')),
	)

	title = models.CharField(_('title'), max_length=200)
	slug = models.SlugField(_('slug'), unique=True, help_text='This slug is the permalink for the post /blog/slug-here/')
	author = models.ForeignKey(User, blank=True, null=True)
	body = models.TextField(_('body'), )
	tease = models.TextField(_('tease'), blank=True, help_text=_('Concise text suggested. Does not appear in RSS feed.'))
	status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
	allow_comments = models.BooleanField(_('allow comments'), default=True)
	publish = models.DateTimeField(_('publish'), default=datetime.datetime.now)
	created = models.DateTimeField(_('created'), auto_now_add=True)
	modified = models.DateTimeField(_('modified'), auto_now=True)
	categories = models.ManyToManyField(Category, blank=True) 

	def __unicode__(self):
		return u'%s' % self.title
