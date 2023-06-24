from django.contrib import admin
from . import models
from django import forms

# @admin.register(models.Poststreams)
# class PoststreamsAdmin(admin.ModelAdmin):
#     list_display = ['description']


# @admin.register(models.Poststreamimage)
# class PoststreamimageAdmin(admin.ModelAdmin):
#     list_display = ['poststream']

# @admin.register(models.Streamslikes)
# class StreamslikesAdmin(admin.ModelAdmin):
#     list_display = ['poststream', 'liked_status']


# @admin.register(models.StreamsComments)
# class StreamsCommentsAdmin(admin.ModelAdmin):
#     list_display = ['poststream', 'comment']

# @admin.register(models.Repliedcomment)
# class RepliedcommentAdmin(admin.ModelAdmin):
#     list_display = ['streamscomment', 'replay_comment','liked_status']
