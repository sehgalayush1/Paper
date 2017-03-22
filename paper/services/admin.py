from django.contrib import admin

from models import *

# Register your models here.
class StoryAdmin(admin.ModelAdmin):
	list_display = ('title', 'timestamp', 'comments')


admin.site.register(Story, StoryAdmin)