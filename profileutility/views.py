from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
import json

from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.http import JsonResponse

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.http import HttpResponseBadRequest
from .serializers import *
from .models import *


@api_view(['POST', ])
@csrf_exempt
def createEquiry(request): 
    requestData = json.loads(request.body)
    ResponseData = None
    try:
        profile_ins = Profile.objects.get(id=requestData['profile'])
        address_ins = ProfileAddress.objects.get(id=requestData['address'])
        rawDistData = Enquirylog.objects.create(
        profile = profile_ins,
        profile_address = address_ins,
        type_of_enq=requestData['type_of_enq'],
        title = requestData['title'],
        list=requestData['list'],
        detail=requestData['detail'],
        mobile=requestData['mobile'],
        email=requestData['email'],
        kmdriven=requestData['kmdriven'],
        price=requestData['price'],
        lat=requestData['lat'],
        long=requestData['long'],
        enquire_at=requestData['enquire_at'],
        scheduled=requestData['scheduled'])
        rawDistData.save()
        ResponseData = {"status":200}
    except Exception as e:
        print(e)
        ResponseData = {"status":status.HTTP_404_NOT_FOUND}
    return Response(ResponseData)       


@api_view(['GET', ])
@csrf_exempt
def getProfile(request, cust_id):
    ResponseData = None 
    if request.method == 'GET':
        try:
            rawDistData = Profile.objects.prefetch_related('profile_address', 'profile_fb', 'profile_preference', 'profile_aoi', 'profile_search', 'activity_profile').filter(id=cust_id)
            serialize = ProfileSerializer(rawDistData, many=True)
            ResponseData = serialize.data
        except Profile.DoesNotExist:
            ResponseData = {"status":status.HTTP_404_NOT_FOUND}
        return Response(ResponseData)   


@api_view(['POST', 'PUT', ])
@csrf_exempt
def profileCU(request): 
    requestData = json.loads(request.body)
    ResponseData = None
    if request.method == 'POST':
        try:
            #We have already created the user when register so add extra detail you have to update the profile
            user = User.objects.get(id=requestData['user'])
            user.first_name = requestData['first_name']
            user.last_name = requestData['last_name']
            user.email = requestData['email']
            user.save()

            rawProfileData = Profile.objects.create(
            phone=requestData['phone'],
            gender=requestData['gender'],
            year_of_birth=requestData['year_of_birth'],
            lat=requestData['lat'],
            long=requestData['long'],
            user=user)
            rawProfileData.save()

            ResponseData = {"status":200}
        except Exception as e:
            print(e)
            ResponseData = {"status":"Profile already exist or Error in creating profile"}
        return Response(ResponseData)

    if request.method == 'PUT':
        try:
            #Update User table
            user = User.objects.get(id=requestData['user'])
            serialize = UserSerializer(user, data=request.data, partial=True)
            if serialize.is_valid():
                serialize.save()

            #Update Profile(Profile Table)
            profile_detail = Profile.objects.get(user_id=requestData['user'])
            serializer = SimpleProfileSerializer(profile_detail, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()

            ResponseData = {"status": '200', 'message': 'update successfully'}

        except Exception as e:
            print(e)
            ResponseData = {"status":'404', 'error': str(e)}
        return Response(ResponseData)    


@api_view(['POST', 'GET', ])
@csrf_exempt
def profileSearch(request): 
    ResponseData = None
    requestData = json.loads(request.body)
    if request.method == 'POST':
        try:
            profile = Profile.objects.get(id=requestData['profile'])
            rawProfileData = ProfileSearch.objects.create(
            profile=profile,
            keyword=requestData['keyword']
            )
            rawProfileData.save()
            ResponseData = {"status":200}
        except Exception as e:
            ResponseData = {"status":status.HTTP_404_NOT_FOUND}
        return Response(ResponseData)

    if request.method == 'GET':
        try:
            c_id=requestData['profile']
            rawDistData = ProfileSearch.objects.filter(profile_id=c_id)
            serialize = ProfileSearchSerializer(rawDistData, many=True)
            ResponseData = serialize.data
        except Exception as e:
            ResponseData = {"status":status.HTTP_404_NOT_FOUND}
        return Response(ResponseData) 


@api_view(['POST', ])
@csrf_exempt
def createWish(request):
    ResponseData = None
    if request.method == 'POST':
        requestData = json.loads(request.body)
        try:
            profile_ins = Profile.objects.get(id=requestData['profile'])
            item_ins = ItemDescription.objects.get(id=requestData['item'])
            rawProfileData = Wishlist.objects.create(profile=profile_ins, item=item_ins)
            rawProfileData.save()

            ResponseData = {"status":200, "id":rawProfileData.id}
        except Exception as e:
            ResponseData = {"status":"profile is exisitig with mention id duplicate entry"}
        return Response(ResponseData)


@api_view(['GET', 'PUT', ])
@csrf_exempt
def makeWish(request,query):
    ResponseData = None
    if request.method == 'GET':
        try:
            rawProfileData = Wishlist.objects.prefetch_related('item').filter(profile_id=query)
            serialize = WishlistSerializer(rawProfileData, many=True)
            ResponseData = serialize.data
        except Exception as e:
            ResponseData = {"status":status.HTTP_404_NOT_FOUND}
        return Response(ResponseData)

    if request.method == 'PUT':
        try:
            rawProfileData = Wishlist.objects.filter(pk=query)
            rawProfileData.delete()
            ResponseData = {"status":200}
        except Exception as e:
            ResponseData = {"status":"profile is exisitig with mention id duplicate entry"}
        return Response(ResponseData)


@api_view(['POST', ])
@csrf_exempt
def custActivity(request):
    requestData = json.loads(request.body)
    ResponseData = None
    if request.method == 'POST':
        try:
            profile_ins = Profile.objects.get(id=requestData['profile'])
            rawProfileData = ProfileActivity.objects.create(profile=profile_ins, 
                                                        type=requestData['type'],
                                                        instance=requestData['instance']
                                                        )
            rawProfileData.save()

            ResponseData = {"status":200}
        except Exception as e:
            ResponseData = {"status":"check the inputs"}
        return Response(ResponseData)        


@api_view(['POST', ])
@csrf_exempt
def userExistance(request):
    """
    POST check existance
    """
    try:
        data = json.loads(request.body)
        phone = data.get('phone')
        ResponseData = None
    

        if phone is None:
            return JsonResponse({
                "errors": {
                    "detail": "Please enter phone number"
                }
            }, status=400)

        # User and Profile Fetch
        rawDistData = Profile.objects.filter(phone=phone)
        
        if not rawDistData:
            ResponseData = {"status":"user does not exist with given phone number!", "error":status.HTTP_404_NOT_FOUND}
        else :
            serialize = ProfileSerializer(rawDistData, many=True)
            ResponseData = serialize.data
        

        return Response(ResponseData)    

    except Exception as e:
        print("Invalid Data Input...")


@api_view(['POST', ])
@csrf_exempt
def login_view(request):
    """
    POST API for login
    """
    ResponseData = {"status":"user does not exist with given credential!", "error":status.HTTP_404_NOT_FOUND}
    try:
        data = json.loads(request.body)
        phone = data.get('phone')
        password = data.get('password')
        if phone is None:
            ResponseData = {"status":"check the  input"}
        elif password is None:
            ResponseData = {"status":"check the  input"}

        user = authenticate(phone=phone, password=password)
        if user is not None:
            login(request, user)
            cust = Profile.objects.values('id').filter(phone=phone)
            cust_id = cust[0]['id']
            ResponseData = {"profile_name":user.username, "profile_id":cust_id}
        return Response(ResponseData)
    except Exception as e:
        print("Invalid Data Input...")


@api_view(['POST', ])
@csrf_exempt
def profileCrm(request): 
    requestData = json.loads(request.body)
    profile = None
    try:
        # create a new PaymentRequest object with the provided data
        profile = Profile.objects.get(phone=requestData['phone'])
    except Exception as e:
        profile = None

    try:

        instance = PaymentRequest(
        internal_profile=profile,
        register_no=requestData.get('register_no', None),
        phone=requestData.get('phone', None),
        name=requestData.get('name', None),
        amount=requestData.get('amount', None),
        purpose=requestData.get('purpose', None),
        requested_employee_id=requestData.get('requested_employee_id', None),
        requested_employee_name=requestData.get('requested_employee_name', None),
        requested_employee_mobile=requestData.get('requested_employee_mobile', None),
        requested_employee_location=requestData.get('requested_employee_location', None)
        )
        instance.save()


        # firebase implementations starts here
        fb_token = ProfileFbtoken.objects.filter(profile_id = profile.id).values('token')

        #  Firebase Curl Implementation


        #  Firebase implementations Ends here


        # return success response
        response_data = {'status': 200, 'message': 'PaymentRequest created successfully.'}
        return Response(response_data)
    except Exception as e:
        # return error response for exceptions
        response_data = {'status': 500, 'message': str(e)}
        if str(e) == "'NoneType' object has no attribute 'id'" :
            response_data = {'status': 200, 'message': 'new Payment Request has been created but customer not initated '}

        return Response(response_data)


@api_view(['GET', 'PUT', ])
@csrf_exempt
def profileCrmRD(request,phone):
    ResponseData = None
    if request.method == 'GET':
        try:
            rawProfileData = PaymentRequest.objects.filter(phone=phone)
            serialize = PaymentRequestSerializer(rawProfileData, many=True)
            ResponseData = serialize.data
        except Exception as e:
            ResponseData = {'status': 500, 'message': str(e)}
        return Response(ResponseData)

    if request.method == 'PUT':
        requestData = json.loads(request.body)
        try:
            profile = PaymentRequest.objects.get(phone=phone)
            profile.phone = requestData['phone']
            profile.name = requestData['name']
            profile.amount = requestData['amount']
            profile.purpose = requestData['purpose']
            profile.requested_employee_id = requestData['requested_employee_id']
            profile.requested_employee_name = requestData['requested_employee_name']
            profile.requested_employee_mobile = requestData['requested_employee_mobile']
            profile.requested_employee_location = requestData['requested_employee_location']
            profile.dont_show = requestData['dont_show']
            profile.save()
            ResponseData = {"status": 200}
        except Exception as e:
            ResponseData = {"status":status.HTTP_404_NOT_FOUND}


@api_view(['POST'])
@csrf_exempt
def crmTransaction(request):
    if request.method == 'POST':
        try:
            transaction_reference_no = request.data.get('transaction_reference_no')
            payment_instance = request.data.get('payment_instance')
            transaction_status = request.data.get('transaction_status', 'pending')
            mode_of_payment = request.data.get('mode_of_payment')
            transaction_date = request.data.get('transaction_date')
            transaction_charge = request.data.get('transaction_charge')
            total_amount_received = request.data.get('total_amount_received')
            remarks = request.data.get('remarks')
            
            profile = Profile.objects.get(id=request.data.get('internal_profile'))
            
            transaction_reference = PaymentTransaction.objects.filter(transaction_reference_no=request.data.get('transaction_reference_no'))
            if not transaction_reference:
                crm_transaction = PaymentTransaction.objects.create(
                    crm_profile=profile,
                    transaction_reference_no=transaction_reference_no,
                    transaction_status=transaction_status,
                    mode_of_payment=mode_of_payment,
                    transaction_date=transaction_date,
                    transaction_charge=transaction_charge,
                    total_amount_received=total_amount_received,
                    remarks=remarks
                )

                crm_transaction.save()
                if transaction_status == 'Success':
                    instance = PaymentRequest.objects.get(id = payment_instance)
                    instance.payment_status = 'Completed'
                    instance.internal_profile = profile
                    instance.save()
                return Response({"status": 201})
            else:
                return Response({"status": 403, "message": "duplicated entry"})

        except Exception as e:
            return Response({"status": status.HTTP_404_NOT_FOUND, "message": str(e)})


@api_view(['PUT', ])
@csrf_exempt
def forgotPassword(request): 
    requestData = json.loads(request.body)
    ResponseData = None
 
    if request.method == 'PUT':
        try:
            phone=requestData['phone']
            profile = Profile.objects.get(phone=phone)
            user = profile.user_id
            user_ins = User.objects.get(id=user)
            user_ins.set_password(requestData['password'])
            user_ins.save()
            serialize = UserSerializer(user_ins)
            ResponseData = {"status": 200, "data":serialize.data}
        except Exception as e:
            ResponseData = {"status":status.HTTP_404_NOT_FOUND}
        return Response(ResponseData) 


#To Get,Delete and update particular address 
@api_view(['PUT', 'GET', 'DELETE'])
@csrf_exempt
def getProfileAddressModify(request,id):
    try:
        if request.method == 'PUT':
            profile_address = ProfileAddress.objects.get(id=id)
            serializer = ProfileAddressSerializer(profile_address, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        if request.method == 'GET':
            data = ProfileAddress.objects.get(id=id)
            serializer = ProfileAddressSerializer(data)
            return Response(serializer.data)

        if request.method == 'DELETE':
            address = get_object_or_404(ProfileAddress, id=id)
            address.delete()
            return Response('200')
    except Exception as e:
        return Response({"status": str(e)})


#Fetch and post address of profile by profile id
@api_view(['GET', 'POST'])
@csrf_exempt
def getAddressByProfile(request,id):
    if request.method == 'GET':
        try:
            profile = Profile.objects.prefetch_related('profile_address').filter(id=id).get()
            serializer = Profile_ProfileAddressSerializer(profile)
            return Response(serializer.data)
        except Exception as e:
            return Response({"status": status.HTTP_404_NOT_FOUND})

    if request.method == 'POST':
        try:
            deserialize = json.loads(request.body)
            # profile_id = deserialize['profile']
            profile = Profile.objects.get(id=id)
            data = ProfileAddress.objects.create(
                profile=profile,
                type_of_address=deserialize['type_of_address'],
                door_no=deserialize['door_no'],
                street=deserialize['street'],
                area=deserialize['area'],
                city=deserialize['city'],
                landmark=deserialize['landmark'],
                lat=deserialize['lat'],
                long=deserialize['long'],
            )
            data.save()
            return Response('Successfully Stored')
        except Exception as e:
            return Response({"status": status.HTTP_404_NOT_FOUND})


#---- Profile FbToken ----
#Fetch and post ProfileFbtoken of profile by profile id
@api_view(['GET','POST'])
@csrf_exempt
def getFbtokenByProfile(request,id):
    if request.method == 'GET':
        try:
            fb_token = ProfileFbtoken.objects.filter(profile_id=id)
            serializer = ProfileFbtokenSerializer(fb_token, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"status":404, "error":str(e)})

    if request.method == 'POST':
        try:
            deserialize = json.loads(request.body)
            profile_id = id
            profile = Profile.objects.get(id=profile_id)
            data = ProfileFbtoken.objects.create(
                profile=profile,
                type_of_token=deserialize['type_of_token'],
                device_name=deserialize['device_name'],
                token=deserialize['token'],
                status = deserialize['status'],
            )
            data.save()
            return Response({"status": 200, "message": "stored successfully"})

        except Exception as e:
            return Response({"status": 500, "error": str(e)})


# #To Get,Delete and update particular Fbtoken
@api_view(['PUT','GET','DELETE'])
@csrf_exempt
def getProfileFbtokenModify(request,id):
    try:

        if request.method == 'PUT':
            profile_Fbtoken = ProfileFbtoken.objects.get(id=id)
            serializer = ProfileFbtokenSerializer(profile_Fbtoken, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        if request.method == 'GET':
            data = ProfileFbtoken.objects.get(id=id)
            serializer = ProfileFbtokenSerializer(data)
            return Response(serializer.data)

        if request.method == 'DELETE':
            address = get_object_or_404(ProfileFbtoken, id=id)
            address.delete()
            return Response('200')
    except Exception as e:
        return Response({"status":400, "error":str(e)})


#---- Profile Aoi ----
#Fetch and post ProfileAoi of profile by profile id
@api_view(['GET','POST'])
@csrf_exempt
def getaoiByProfile(request,id):
    try:
        if request.method == 'GET':
            # profile = Profile.objects.prefetch_related('profile_aoi').filter(id=id).get()
            # serializer = Profile_ProfileAoiSerializer(profile)
            profile_aoi = ProfileAoi.objects.filter(profile_id=id)
            serializer = ProfileAoiSerializer(profile_aoi, many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            deserialize= json.loads(request.body)
            profile_id = id
            profile = Profile.objects.get(id=profile_id)
            data = ProfileAoi.objects.create(profile = profile,
                                              type = deserialize['type'],
                                              interest = deserialize['interest'],
                                              remarks = deserialize['remarks']
                                              )
            data.save()
            return Response('Successfully Stored')
    except Exception as e:
        return Response({"status":400, "error":str(e)})

#
#To Get, Delete and update particular Fbtoken
@api_view(['PUT','GET','DELETE'])
@csrf_exempt
def getProfileaoiModify(request,id):
    try:
        if request.method == 'PUT':
            profile_Aoi = ProfileAoi.objects.get(id=id)
            serializer = ProfileAoiSerializer(profile_Aoi, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)
        if request.method == 'GET':
            data = ProfileAoi.objects.get(id=id)
            serializer = ProfileAoiSerializer(data)
            return Response(serializer.data)
        if request.method == 'DELETE':
            address = get_object_or_404(ProfileAoi, id=id)
            address.delete()
            return Response('200')
    except Exception as e:
        return Response({"status":400, "error":str(e)})


#---- Profile Notification preference ----
#Fetch and post Profile preference of profile by profile id
@api_view(['GET','POST'])
@csrf_exempt
def getnotficationByProfile(request,id):
    try:
        if request.method == 'GET':
            profile_np = ProfileNoticationPreference.objects.filter(profile_id=id)
            serializer = ProfileNoticationPreferenceSerializer(profile_np, many=True)
            return Response(serializer.data)

        if request.method == 'POST':
            deserialize= json.loads(request.body)
            profile_id = id
            profile = Profile.objects.get(id=profile_id)
            data = ProfileNoticationPreference.objects.create(profile = profile,
                                              type_of_notification = deserialize['type_of_notification'],
                                              status = deserialize['status']
                                              )
            data.save()
            return Response('Successfully Stored')
    except Exception as e:
        return Response({"status":400, "error":str(e)})


#To Get, Delete and update particular Notification
@api_view(['PUT','GET','DELETE'])
@csrf_exempt
def getProfileanoticationModify(request,id):
    try:
        if request.method == 'PUT':
            profile_np = ProfileNoticationPreference.objects.get(id=id)
            serializer = ProfileNoticationPreferenceSerializer(profile_np, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data)

        if request.method == 'GET':
            data = ProfileNoticationPreference.objects.get(id=id)
            serializer = ProfileNoticationPreferenceSerializer(data)
            return Response(serializer.data)

        if request.method == 'DELETE':
            address = get_object_or_404(ProfileNoticationPreference, id=id)
            address.delete()
            return Response('200')

    except Exception as e:
        return Response({"status":400, "error":str(e)})


# @api_view(['GET'])
# @csrf_exempt
# def empPaymentReq(request, emp_id):
#     try:
#         if request.method == 'GET':
#             data = PaymentRequest.objects.filter(requested_employee_id = emp_id)
#             serialize = PaymentRequestSerializer(data, many=True)
#             return Response(serialize.data)
#     except Exception as e:
#         return Response({"status":400, "message":str(e)})    