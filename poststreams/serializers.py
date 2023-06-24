from rest_framework import serializers
from .models import *


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile  # Replace "Profile" with your actual model name
        fields = '__all__' 

class PoststreamimageSerializer(serializers.ModelSerializer):
     class Meta:
          model = Poststreamimage
          fields = ["poststream", "emoji",'image']

class StreamslikesSerializer(serializers.ModelSerializer):
     class Meta:
        model = Streamslikes
        fields = '__all__'

class  RepliedcommentlikesSerializer(serializers.ModelSerializer):
     class Meta:
        model =  Repliedcommentlikes
        fields = '__all__' 

class  RepliedcommentSerializer(serializers.ModelSerializer):
     repliedcommentlike = RepliedcommentlikesSerializer(many=True)
     class Meta:
        model =  Repliedcomment
        fields = ['replay_comment','streamscomment','user','repliedcommentlike'] 
 
class StreamscommentsLikesSerializer(serializers.ModelSerializer):
     class Meta:
        model = StreamscommentsLikes
        fields = '__all__'

class  StreamspamSerializer(serializers.ModelSerializer):
     class Meta:
        model = Streamspam
        fields = '__all__'

class StreamsCommentsSerializer(serializers.ModelSerializer):
     streamrlpcom = RepliedcommentSerializer(many=True)
     streamscommentslike = StreamscommentsLikesSerializer(many=True)
     class Meta:
        model = Streamscomments
        fields = ['user','poststream','comment','streamscommentslike','streamrlpcom'] 


# Get all idetails
class PostStreamsSerializer(serializers.ModelSerializer):
     stream = PoststreamimageSerializer(many=True)
     streamlike = StreamslikesSerializer(many=True)
     streamcom = StreamsCommentsSerializer(many=True)
     class Meta:
          model = Poststreams   
          fields = ['description','post_status', 'stream','streamlike','streamcom'] 


class PostStreamsCreateSerializer(serializers.ModelSerializer):
     class Meta:
          model = Poststreams   
          fields = '__all__'     

class AddCommentsSerializer(serializers.ModelSerializer):
     class Meta:
        model = Streamscomments
        fields = '__all__'


class  AddRepliedcommentSerializer(serializers.ModelSerializer):
     class Meta:
        model =  Repliedcomment
        fields = '__all__'

