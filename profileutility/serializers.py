from rest_framework import serializers
from .models import *
from showcase.models import ItemDescription
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer


class EnquirylogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquirylog
        fields = ['type_of_enq', 'title', 'list', 'detail', 'mobile', 'email', 'remarks', 'kmdriven', 'price', 'enquire_at', 'scheduled'] 


class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password',
                  'email', 'first_name', 'last_name']


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']


class GetItemDescriptionSerializer(serializers.ModelSerializer):   
        class Meta:
            model = ItemDescription
            fields = ['id', 'title','subtitle', 'itemlist', 'color', 'price', 'images', 'description', 'about', 'page_navigation', 'spec']


class WishlistSerializer(BaseUserSerializer):
    item = GetItemDescriptionSerializer()
    class Meta:
        model = Wishlist
        fields = ['id', 'profile', 'item']


class ProfileActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileActivity
        fields = '__all__'

class ProfileAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileAddress
        fields = '__all__'

class ProfileFbtokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileFbtoken
        fields = ['id', 'type_of_token', 'device_name', 'token', 'status']

class ProfileAoiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileAoi
        fields = ['id', 'type', 'interest', 'remarks']

class ProfileNoticationPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileNoticationPreference
        fields = '__all__'

class ProfileSearchSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProfileSearch
        fields = ['keyword', 'search_at']

class SimpleProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    profile_address = ProfileAddressSerializer(many=True)
    profile_fb = ProfileFbtokenSerializer(many=True)
    profile_preference = ProfileNoticationPreferenceSerializer(many=True)
    profile_aoi = ProfileAoiSerializer(many=True)
    profile_search = ProfileSearchSerializer(many=True)
    activity_profile = ProfileActivitySerializer(many=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'year_of_birth', 'membership', 'profile_address', 'profile_fb', 'profile_preference', 'profile_aoi', 'profile_search', 'activity_profile']


class ProfileUserSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['id', 'user', 'phone', 'year_of_birth', 'membership']


class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = '__all__'

class GetSimpleItemDescriptionSerializer(serializers.ModelSerializer):   
        class Meta:
            model = ItemDescription
            fields = ['id', 'title','subtitle', 'color', 'price', 'images']


class PaymentRequestSerializer(serializers.ModelSerializer):
    # item = GetSimpleItemDescriptionSerializer()

    class Meta:
        model = PaymentRequest
        fields = ['id', 'register_no', 'payment_status', 'phone', 'name', 'amount', 'purpose', 'requested_employee_name', 'created_at', 'modified_at']


class Profile_ProfileAddressSerializer(serializers.ModelSerializer):
	profile_address = ProfileAddressSerializer(many=True)

	class Meta:
		model = Profile
		fields = ['id','phone', 'profile_address']
                
                
class Profile_ProfileFbtokenSerializer(serializers.ModelSerializer):
	profile_fb = ProfileFbtokenSerializer(many=True)

	class Meta:
		model = Profile
		fields = ['id','phone', 'profile_fb']

                

class Profile_ProfileAoiSerializer(serializers.ModelSerializer):
	profile_aoi = ProfileAoiSerializer(many=True)

	class Meta:
		model = Profile
		fields = ['id','phone', 'profile_aoi']        