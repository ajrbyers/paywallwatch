from django.contrib import admin

from models import Post, Category

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created', 'publish', 'status')
    search_fields = ('title',)
    save_as = True

class CategortAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug')
	search_fields = ('title', 'slug')
	save_as = True

admin_list = [
    (Post, PostAdmin),
    (Category, CategortAdmin),
]

[admin.site.register(*t) for t in admin_list]