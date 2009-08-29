# -*- coding: utf-8 -*-

from django.contrib import admin
from rumpleteazer.articles.models import Series, Article

class SeriesAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title', 'published', 'status', 'summary')
	list_filter = ('published', 'series', 'status')
	search_fields = ('title', 'body')


admin.site.register(Series, SeriesAdmin)
admin.site.register(Article, ArticleAdmin)
