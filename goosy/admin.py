from django.contrib import admin
from djangohomework.goosy import models

# Register your models here.
class TrackAdmin(admin.ModelAdmin):
    #list_display = ['track_title', 'track_author', 'track_description', 'track_duration']
    list_display = ['track_title', 'track_author', 'track_album']
admin.site.register(models.Track, TrackAdmin)