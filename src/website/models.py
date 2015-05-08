from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.db.models import permalink
from django.contrib.auth.models import User
from django.conf import settings

import datetime

# Create your models here.

class Page(models.Model):
	STATUS_CHOICES = (
		(1, _('Draft')),
		(2, _('Public')),
	)

	title = models.CharField(_('title'), max_length=200)
	slug = models.SlugField(_('slug'), unique_for_date='publish', help_text='This makes up the page url /about/ or /board/')
	author = models.ForeignKey(User, blank=True, null=True)
	body = models.TextField(_('body'), )
	status = models.IntegerField(_('status'), choices=STATUS_CHOICES, default=2)
	publish = models.DateTimeField(_('publish'), default=datetime.datetime.now)
	created = models.DateTimeField(_('created'), auto_now_add=True)
	modified = models.DateTimeField(_('modified'), auto_now=True)

	def __unicode__(self):
		return u'%s' % self.title