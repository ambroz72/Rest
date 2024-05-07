from . models import Task
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):  
    password = serializers.CharField(write_only=True)
    
    def create(self,validated_date):
        user=get_user_model().objects.create(username=validated_date['username'])
        user.set_password(validated_date['password'])
        user.save()
        return user
    class Meta:
        model=get_user_model()
        fields=('username','password')

class TaskSerializers(serializers.ModelSerializer):
    image=serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model=Task
        fields=['id','task_name','task_desc','completed','date_created','image']
        

