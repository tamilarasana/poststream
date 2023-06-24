from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json
import os
from .models import *
from .serializers import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
@api_view(['POST'])
@csrf_exempt
def createProfile(request):
    if request.method == 'POST':
        requestData = json.loads(request.body)
        ResponseData = None
        if request.method == 'POST':
            try:
                ProfileData = Profile.objects.create(
                    username=requestData['username'],
                    phone=requestData['phone'],
                    email = requestData['email'],
                    password = make_password(requestData['password'])
                )
                ResponseData = {"status":200}
            except Exception as e:
                ResponseData = {"status":"Email already exist or Error in creating New Email"}
        return Response(ResponseData)


@api_view(['GET','POST']) 
@csrf_exempt
def getStreams(request):

    if request.method == 'GET':
        poststream = Poststreams.objects.prefetch_related('stream','streamlike','streamcom').filter(post_status = 'Active')
        serializer = PostStreamsSerializer(poststream, many=True)
        likes = Streamslikes.objects.all()
        comments = Streamscomments.objects.all()
        streamreplied = Repliedcomment.objects.all()
        total_comments = comments.count() + streamreplied.count()
        user_liked_or_not = request.GET.get('user_liked_or_not')
        userlikerOrnot = Streamslikes.objects.filter(poststream = user_liked_or_not).exists()
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK,'total_likes': likes.count(), 'total_comments':total_comments, 'userlikeroRnot':userlikerOrnot})
   
    if request.method == 'POST':
        serializer = PostStreamsCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})
    


# Get Poststream Image .
@api_view(['GET','POST'])
def getStreamsImage(request):
    if request.method == 'GET':
        poststreamimg  = Poststreamimage.objects.all()
        serializer = PoststreamimageSerializer(poststreamimg, many=True)
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})
    
    if request.method == 'POST':
        images = request.FILES.getlist('image')
        poststream_id = request.data['poststream']
        poststream = Poststreams.objects.get(id=poststream_id)
        emoji = request.data.get('emoji')
        for image in images:
            post = Poststreamimage.objects.create(image=image, poststream = poststream, emoji=emoji)
            post.save()
        return Response({"status":status.HTTP_200_OK})


# Streamslikes .
@api_view(['GET', 'POST'])
def getStreamsLike(request):
    if request.method == 'GET':
        streamlike = Streamslikes.objects.all()
        serializer = StreamslikesSerializer(streamlike, many=True)
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})

    if request.method == 'POST':
        serializer = StreamslikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})


# Streams Comment .
@api_view(['GET','POST'])
def getStreamsComment(request):
    if request.method == 'GET':
        streamcomment = Streamscomments.objects.all()
        serializer = AddCommentsSerializer(streamcomment, many=True)
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})

    if request.method == 'POST':
        serializer = AddCommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})


# Streams Replied Comment .
@api_view(['GET','POST'])
@csrf_exempt
def getStreamscommentsLikes(request):
    if request.method == 'GET':
        streamrepliedlikes = StreamscommentsLikes.objects.all()
        serializer = StreamscommentsLikesSerializer(streamrepliedlikes, many=True)
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})

    if request.method == 'POST':
        serializer = StreamscommentsLikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})


# Streams Replied Comment .
@api_view(['GET','POST'])
@csrf_exempt
def getStreamsRepliedComment(request):
    if request.method == 'GET':
        streamreplied = Repliedcomment.objects.all()
        serializer = AddRepliedcommentSerializer(streamreplied, many=True)
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})

    if request.method == 'POST':
        serializer = AddRepliedcommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})

     
# Streams Replied Comment .
@api_view(['GET','POST'])
@csrf_exempt
def getRepliedcommentlikes(request):
    if request.method == 'GET':
        streamrepliedlikes = Repliedcommentlikes.objects.all()
        serializer = RepliedcommentlikesSerializer(streamrepliedlikes, many=True)
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})

    if request.method == 'POST':
        serializer = RepliedcommentlikesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})


# Streams Replied Comment .
@api_view(['GET','POST'])
@csrf_exempt
def getStreamSpam(request):
    if request.method == 'GET':
        streamspam= Streamspam.objects.all()
        serializer = StreamspamSerializer(streamspam, many=True)
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})

    if request.method == 'POST':
        serializer = StreamspamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response({"data":serializer.data ,"status":status.HTTP_200_OK})

# Remove Like 
@api_view(['POST'])
@csrf_exempt
def changeStreampostStatus(request):
    streamcomment = request.GET.get('poststream_id')
    poststream = Poststreams. objects.get( id = streamcomment )
    if poststream.post_status == 'Active':
      streamspam = Poststreams.objects.update( post_status = "Inactive")
    message = "StreamPost Deleted"
    return Response({"status":status.HTTP_200_OK, "message" : message})

# Remove Like 
@api_view(['DELETE'])
@csrf_exempt
def removeStreamsLike(request):
    stream_id = request.GET.get('poststream_id')
    user_id = request.GET.get('user_id')
    poststream = Streamslikes. objects.get( poststream_id = stream_id, user_id = user_id )
    poststream.delete()
    message = "Post unliked"
    return Response({"status":status.HTTP_200_OK, "message" : message})

@api_view(['DELETE'])
@csrf_exempt
def removeRepliedcommentlikes(request):
    repliedcomment = request.GET.get('repliedcomment_id')
    user_id = request.GET.get('user_id')
    repliedcommentlike = Repliedcommentlikes. objects.get( repliedcomment_id = repliedcomment, user_id = user_id )
    repliedcommentlike.delete()
    message = "ReliedComment unliked"
    return Response({"status":status.HTTP_200_OK, "message":message})

@api_view(['DELETE'])
@csrf_exempt
def removeStreamscommentsLikes(request):
    streamscommentlike = request.GET.get('streamscommentlike_id')
    user_id = request.GET.get('user_id')
    repliedcommentlike = StreamscommentsLikes.objects.get( streamscommentlike_id  = streamscommentlike, user_id = user_id )
    repliedcommentlike.delete()
    message = "Stream Comment unliked"
    return Response({"status":status.HTTP_200_OK, "message": message})


@api_view(['DELETE'])
@csrf_exempt
def removeStreamscomments(request):
    streamcomment = request.GET.get('streamcomment_id')
    user_id = request.GET.get('user_id')
    streamcomment= Streamscomments.objects.get(id = streamcomment, user_id = user_id)
    streamcomment.delete()
    message = "Stream Comment Deleted Successfully"
    return Response({"status":status.HTTP_200_OK, "message": message})


@api_view(['DELETE'])
@csrf_exempt
def removeReplycomment(request):
    replycomment = request.GET.get('replycomment_id')
    user_id = request.GET.get('user_id')
    replycomment= Repliedcomment.objects.get(id = replycomment, user_id = user_id)
    replycomment.delete()
    message = "Stream Comment Deleted Successfully"
    return Response({"status":status.HTTP_200_OK, "message": message})






