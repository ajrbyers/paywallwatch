from django.contrib import admin

from models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'publish', 'status')
    search_fields = ('title',)

admin_list = [
    (Page, PageAdmin),
]

[admin.site.register(*t) for t in admin_list]