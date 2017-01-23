# -*- coding: utf-8 -*-
from django.contrib import admin

from app.models import *

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    prepopulated_fields = {'slug': ('name',)}


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'posted_date')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(App_News, NewsAdmin)