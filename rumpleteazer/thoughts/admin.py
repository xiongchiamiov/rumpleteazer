# -*- coding: utf-8 -*-

from django.contrib import admin
from rumpleteazer.thoughts.models import Post

class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'published', 'status', 'tags', 'summary')
	list_filter = ('published', 'status')
	search_fields = ('title', 'body')


admin.site.register(Post, PostAdmin)
