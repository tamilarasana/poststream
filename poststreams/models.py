from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    username = models.CharField(max_length=255, null=True,blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
    password = models.CharField(max_length=128, null=True, blank=True)

class Poststreams(models.Model):
    
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    ACTIVE_STATUS = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    description = models.TextField()
    post_status = models.CharField(max_length=50, choices=ACTIVE_STATUS, default=ACTIVE)

class Poststreamimage(models.Model):
    poststream = models.ForeignKey(Poststreams, on_delete=models.CASCADE, related_name="stream")
    background_image = models.ImageField(upload_to='store/backgroundimage', null=True, blank=True, default=0)
    emoji = models.CharField(max_length=255, null=True, blank=True)
    feelings = models.CxamharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='store/streamimages', null=True, blank=True)

class Streamslikes(models.Model):
    poststream = models.ForeignKey(Poststreams, on_delete=models.CASCADE, related_name='streamlike')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,)
      
    class Meta:
        unique_together = ('poststream', 'user')

class Streamscomments(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE,)
    poststream = models.ForeignKey(Poststreams, on_delete=models.CASCADE, related_name='streamcom')
    comment = models.CharField(max_length=255, null=True)

class Repliedcomment(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    streamscomment = models.ForeignKey(Streamscomments, on_delete=models.CASCADE, related_name='streamrlpcom')
    replay_comment = models.CharField(max_length=255, null=True)
 
class StreamscommentsLikes(models.Model):
    streamscommentlike = models.ForeignKey(Streamscomments, on_delete=models.CASCADE , related_name="streamscommentslike")
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('streamscommentlike', 'user')

class Repliedcommentlikes(models.Model):
    repliedcomment = models.ForeignKey(Repliedcomment, on_delete=models.CASCADE, related_name='repliedcommentlike')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
            unique_together = ('repliedcomment', 'user')

class Streamspam(models.Model):
    poststream = models.ForeignKey(Poststreams, on_delete=models.CASCADE, related_name='streamspam')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('poststream', 'user')



