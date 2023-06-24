from unicodedata import name
from unittest.mock import patch
from django.urls import path
from .views import *

urlpatterns = [

   
    path('create_profile/', createProfile, name="profile"),

    path('get_streams/', getStreams, name="poststream"),
    # path('stream_update_delete_get/<int:id>', getStreamsModify, name="stream_update_delete_get"), #id - address PK

    path('get_streamsimg/', getStreamsImage, name="poststreamimg"),
    # path('streamimg_update_delete_get/<int:id>', getStreamsImageModify, name="streamimg_update_delete_get"),

    path('get_streamslike/', getStreamsLike, name="poststreamlike"),
    # path('streamlike_update_delete_get/<int:id>', getStreamsLikeModify, name='streamlike_update_delete_get'),
   
    path('get_streamscomment/', getStreamsComment, name="poststreamcomment"),

    path('get_streamsreplied/', getStreamsRepliedComment, name="poststreamreplied"),

    path('get_streamspam/', getStreamSpam, name="ststreamspam"),
    
    path('change_postspam/', changeStreampostStatus, name="change_postspam"),

    path('get_streamsrepliedlike/', getRepliedcommentlikes, name="streamsrepliedlike"),
    path('get_streamscommentslike/', getStreamscommentsLikes, name="streamscommentslike"),

    path('remove_streamslike/', removeStreamsLike, name="removestreamslike"),
    path('remove_repcommentlike/', removeRepliedcommentlikes, name="remove_repcommentlike"),
    path('remove_streamcommlike/', removeStreamscommentsLikes, name="remove_streamcommlike"),


    path('remove_streamscomment/', removeStreamscomments, name="remove_streamscomment"),
    path('remove_replycomment/', removeReplycomment, name="remove_replycomment"),


]
