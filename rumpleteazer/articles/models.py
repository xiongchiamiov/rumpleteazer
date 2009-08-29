# -*- coding: utf-8 -*-

from django.db import models

class Series(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique=True)
	summary = models.TextField(blank=True)

	class Meta:
		verbose_name_plural = 'Series'
		ordering = ('title',)

	def __unicode__(self):
		return u'%s' % self.title


STATUS_CHOICES = (
	('Draft', 'Draft'),
	('Public', 'Public'),
)

class Article(models.Model):
	title = models.CharField(max_length=200)
	slug = models.SlugField(unique_for_date='published')
	summary = models.TextField(blank=True)
	body = models.TextField()
	status = models.CharField(choices=STATUS_CHOICES, default='Draft', max_length=20)
	published = models.DateTimeField()
	modified = models.DateTimeField(auto_now=True)
	series = models.ForeignKey(Series, null=True)

	class Meta:
		ordering = ('-published',)

	def __unicode__(self):
		return u'%s' % self.title
