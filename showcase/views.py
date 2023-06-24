from venv import create
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import json
from django.shortcuts import render
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from .models import *
from django.db.models import Q
from profileutility.models import ProfileSearch, Profile, PaymentRequest
from django.utils import timezone


@api_view(['GET', ])
@csrf_exempt
def getCategory(request): 
    ResponseData = None
    try:
        category = Category.objects.all()
        serialize = CategorySerializer(category, many=True) 
        ResponseData = serialize.data

        try:
            now = timezone.now()
            expired_requests = PaymentRequest.objects.filter( payment_status='Pending',created_at__lt=now - timezone.timedelta(hours=24))
            expired_requests.update(payment_status='Expired')

        except Exception as e:
            return Response({"status":str(e)})    

    except Category.DoesNotExist:
        ResponseData = {"status":status.HTTP_404_NOT_FOUND}
    return Response(ResponseData)   


@api_view(['GET', ])
@csrf_exempt
def getItemList(request, key): 
    ResponseData = None
    try:
        rawDistData = Itemlist.objects.filter(category=key)
        serialize = ItemlistSerializer(rawDistData, many=True)
        ResponseData = serialize.data
    except Itemlist.DoesNotExist:
        ResponseData = {"status":status.HTTP_404_NOT_FOUND}
    return Response(ResponseData)   


@api_view(['GET', ])
@csrf_exempt
def getItemDescDist(request, key):
    
    try:
        rawDistData = ItemDescription.objects.order_by('?').filter(itemlist=key)
    except ItemDescription.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serialize = ItemDescriptionSerializer(rawDistData, many=True)
    
    lookup = []
    outPut = []
    data = []
    for i in serialize.data:
        lookup.append(i['title'])

    for id, title in enumerate(lookup):
        if title not in outPut:
            outPut.append(title)
            data.append(serialize.data[id])

    return Response(data) 


@api_view(['GET', ])
@csrf_exempt
def getItemDesc(request, key): 
    ResponseData = None
    try:
        rawDistData = ItemDescription.objects.prefetch_related('spec').filter(id=key)
        serialize = GetItemDescriptionSerializer(rawDistData, many=True)
        ResponseData = serialize.data
    except ItemDescription.DoesNotExist:
        ResponseData = {"status":status.HTTP_404_NOT_FOUND}
    return Response(ResponseData) 


@api_view(['POST', ])
@csrf_exempt
def getColorItemDesc(request): 
    ResponseData = None
    val = json.loads(request.body)
    title = val["title"]
    try:
        rawDistData = ItemDescription.objects.prefetch_related('spec').filter(title=title)
        serialize = GetItemDescriptionSerializer(rawDistData, many=True) 
        ResponseData = serialize.data   
    except ItemDescription.DoesNotExist:
        ResponseData = {"status":status.HTTP_404_NOT_FOUND}
    return Response(ResponseData)


@api_view(['POST', ])
@csrf_exempt
def search_item(request):
    # profile = None
    ResponseData = None
    requestData = json.loads(request.body)
    search_query = requestData["keyword"]
    cust_id = requestData['profile_id']
    try:
        # create a new PaymentRequest object with the provided data
        profile = Profile.objects.get(id=cust_id)
    except Exception as e:
        profile = None

    createSearch = ProfileSearch.objects.create(
        profile=profile,
        keyword=search_query
    )
    createSearch.save()
    
    if search_query:
        items = ItemDescription.objects.filter(
            Q(subtitle__icontains=search_query)
        )
        serialize = ItemDescriptionSerializer(items, many=True)
        
        ResponseData = {"items":serialize.data}
    else:
        ResponseData = {"status":status.HTTP_404_NOT_FOUND}        
    return Response(ResponseData)

def react_home(request, path):
    return render(request, 'index.html', context={"b":"a"})

def r_home(request):
    return render(request, 'index.html', context={"b":"a"})
