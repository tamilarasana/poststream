from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import *
from .models import *
from rest_framework import status
from django.contrib.sessions.models import Session

from .serializers import *
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
import requests
import json


# Create your views here.

@api_view(['GET', 'POST'])
@csrf_exempt
def appBooking(request):
    if request.method == 'GET':
        category_data = AppBooking.objects.all()
        serialize = AppBookingSerializers(category_data, many=True)
        return Response({'status': 200, 'data': serialize.data})

    elif request.method == 'POST':
        serializer = AppBookingSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'data': serialize.data})
        return Response({'status': 400, 'data': serialize.errors})
    
# App Booking Edit Update and Delete
@api_view(['GET', 'PUT','DELETE'])
@csrf_exempt
def appBookingUD(request, id):
    try:
        detail = AppBooking.objects.get(id=id)
    except AppBooking.DoesNotExist:
        return Response({'status': 404, 'data': 'App Booking does not exist'})

    if request.method == 'GET':
        serializer = AppBookingSerializers(detail)
        return Response({'status': 200, 'data': serializer.data})

    if request.method == 'PUT':
        serializer = AppBookingSerializers(AppBooking, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 200, 'data': serializer.data})
        return Response({'status': 400, 'data': serializer.errors})

    if request.method == 'DELETE':
        detail.delete()
        return Response({'status': 200, 'data': 'data deleted successfully'})


# New Car Booking
@api_view(['GET', 'POST'])
@csrf_exempt
def newCarBooking(request):
    if request.method == 'GET':
        newcarbooking = NewCarBooking.objects.all()
        serializer = NewCarBookingSerializers(newcarbooking, many=True)
        return Response({'status': 200, 'data': serializer.data})
    
    if request.method == 'POST':
        serializer = NewCarBookingSerializers(data=request.data)
        if serializer.is_valid():            
            serializer.save()

        url = 'http://superapi.kalyanicrm.com:8080/api/v1/NewCarBooking' 
        payload = json.dumps({
            
            "firstName"             : request.data.get('name'),
            "emailAddress"          : request.data.get('email'),    
            "customerID"            : request.data.get('cust_id_or_reg_no'),
            "addressCity"           : request.data.get('city'),
            "outlet"                : request.data.get('outlets'), 
            "exPrice"               : request.data.get('item_price'),
            "employeeId"            : request.data.get('employee_id'), 
            "referredBy"            : request.data.get('referred_by'),
            "bookingStatus"         : request.data.get('booking_status'),
            # "profile"               : request.data.get('profile'),
            # "description"           : request.data.get('item_description'),
            # "addressStreet"         : request.data.get('address'),
            # "bookingId"             : request.data.get('booking_id'),
            # "phoneNumber"           : request.data.get('mobile'),

        })
        
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWRtaW46MTIzNDU=',
        'Cookie': 'csrftoken=ydHI7HRyRqvPJIEQzG14gXseZo0JmRiB; sessionid=eqwjgobenk17s79za5t1n0y4l43l8mj6'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
    # try:
       
    # except Exception as e:
    #     return Response({'status':200, "data":str(e)})
    
    return Response({'status': 200, 'data': serializer.data})
    return Response({'status': 400, 'data': serializer.errors})
    

    


# New Car Edit Update and Delete
@api_view(['GET', 'PUT','DELETE'])
@csrf_exempt
def newCarBookingUD(request, id):
    try:
        detail = NewCarBooking.objects.get(id=id)
    except NewCarBooking.DoesNotExist:
        return Response({'status': 404, 'data': 'New Car does not exist'})

    if request.method == 'GET':
        serialize = NewCarBookingSerializers(detail)
        return Response({'status': 200, 'data': serialize.data})

    if request.method == 'PUT':
        serialize = NewCarBookingSerializers(AppBooking, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'status': 200, 'data': serialize.data})
        return Response({'status': 400, 'data': serialize.errors})

    if request.method == 'DELETE':
        detail.delete()
        return Response({'status': 200, 'data': 'data deleted successfully'})


# Used Car Booking
@api_view(['GET', 'POST'])
@csrf_exempt
def usedCarBooking(request):
    if request.method == 'GET':
        usedcarbooking = UsedCarBooking.objects.all()
        serialize = UsedCarBookingSerializers(usedcarbooking, many=True)
        return Response({'status': 200, 'data': serialize.data})
    
    elif request.method == 'POST':
        serialize = UsedCarBookingSerializers(data=request.data)
        if serialize.is_valid():
            serialize.save()
        url = 'http://superapi.kalyanicrm.com:8080/api/v1/UsedCarBooking' 
        payload = json.dumps({
            "firstName": request.data.get('name'), 
            "lastName": " ",
            "emailAddress": request.data.get('email'), 
            "phoneNumber": request.data.get('phone'), 
            "kmsDrivenStarting": request.data.get('kms_driven_starting'), 
            "kmsDrivenEnding": request.data.get('kms_driven_ending'), 
            "brand": request.data.get('brand'),
            "model": request.data.get('model'),
            "transmission": request.data.get('transmission'),
            "fuel": request.data.get('fuel'),
            "kmsStart": request.data.get('kms_driven_starting'), 
            "kmsEnd": request.data.get('kms_driven_ending'), 
            "expectedPrice": request.data.get('price'),
            "employeeId": request.data.get('employee_id'),
            "referredBy": request.data.get('referred_by'),
            "enquireAt": request.data.get('enquire_at'),
        })
        
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWRtaW46MTIzNDU=',
        'Cookie': 'csrftoken=ydHI7HRyRqvPJIEQzG14gXseZo0JmRiB; sessionid=eqwjgobenk17s79za5t1n0y4l43l8mj6'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        
        return Response({'status': 200, 'data': serialize.data})
        return Response({'status': 400, 'data': serialize.errors})
    

# Used Car Edit Update and Delete
@api_view(['GET', 'PUT','DELETE'])
@csrf_exempt
def usedCarBookingUD(request, id):
    try:
        detail = UsedCarBooking.objects.get(id=id)
    except UsedCarBooking.DoesNotExist:
        return Response({'status': 404, 'data': 'Car does not exist'})

    if request.method == 'GET':
        serialize = UsedCarBookingSerializers(detail)
        return Response({'status': 200, 'data': serialize.data})

    if request.method == 'PUT':
        serialize = UsedCarBookingSerializers(AppBooking, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'status': 200, 'data': serialize.data})
        return Response({'status': 400, 'data': serialize.errors})

    if request.method == 'DELETE':
        detail.delete()
        return Response({'status': 200, 'data': 'data deleted successfully'})

# Service Booking
@api_view(['GET', 'POST'])
@csrf_exempt
def serviceBooking(request):
    if request.method == 'GET':
        service = Service.objects.all()
        serialize = ServiceSerializers(service, many=True)
        return Response({'status': 200, 'data': serialize.data})
    
    elif request.method == 'POST': 
        serialize = ServiceSerializers(data=request.data)
        if serialize.is_valid():
            serialize.save()

            url = 'http://superapi.kalyanicrm.com:8080/api/v1/ServiceBooking' 

            payload = json.dumps({              
                "firstName": request.data.get('name'),
                "lastName":" ",
                "emailAddress": request.data.get('email'),
                "phoneNumber": request.data.get('mobile'),
                "city": request.data.get('city'),
                "color": request.data.get('color'), 
                "varient": request.data.get('varient'), 
                "employeeId": request.data.get('employee_id'), 
                "referredId": request.data.get('referred_id'), 
                "bookingStatus": request.data.get('booking_status'), 
                "outlets": request.data.get('outlet'), 
                "itemPrice": request.data.get('item_price'),    
                "bookingId": request.data.get('booking_id'),    
            })
        
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic YWRtaW46MTIzNDU=',
        'Cookie': 'csrftoken=ydHI7HRyRqvPJIEQzG14gXseZo0JmRiB; sessionid=eqwjgobenk17s79za5t1n0y4l43l8mj6'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        
        return Response({'status': 200, 'data': serialize.data})
        return Response({'status': 400, 'data': serialize.errors})

# Service Edit Update and Delete
@api_view(['GET', 'PUT','DELETE'])
@csrf_exempt
def serviceBookingUD(request, id):
    try:
        detail = Service.objects.get(id=id)
    except Service.DoesNotExist:
        return Response({'status': 404, 'data': 'Car does not exist'})

    if request.method == 'GET':
        serialize = ServiceSerializers(detail)
        return Response({'status': 200, 'data': serialize.data})

    if request.method == 'PUT':
        serialize = ServiceSerializers(AppBooking, data=request.data)
        if serialize.is_valid():
            serialize.save()
            return Response({'status': 200, 'data': serialize.data})
        return Response({'status': 400, 'data': serialize.errors})

    if request.method == 'DELETE':
        detail.delete()
        return Response({'status': 200, 'data': 'data deleted successfully'})
