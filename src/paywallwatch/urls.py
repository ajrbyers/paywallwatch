"""paywallwatch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^summernote/', include('django_summernote.urls')),

    url(r'^$', 'website.views.home', name='home'),
    url(r'^about/$', 'website.views.about', name='about'),

    # Admin Dash
    url(r'^dashboard/$', 'website.views.dashboard', name='dashboard'),
    url(r'^dashboard/blog/new/', 'blog.views.new', name='new'),
    url(r'^dashboard/blog/edit/(?P<slug>[-\w]+)/$', 'blog.views.edit', name='edit'),

    url(r'^dashboard/page/new/$', 'website.views.new', name='new_page'),
    url(r'^dashboard/page/edit/(?P<slug>[-\w]+)/$', 'website.views.edit', name='edit_page'),

    # Auth URLS
    url(r'^login/$', 'website.views.login', name='login'),
    url(r'^logout/$', 'website.views.logout', name='logout'),

    # Custom Pages
    url(r'^(?P<page>[-\w]+)/$', 'website.views.page', name='page'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)