from dataclasses import fields
from rest_framework import serializers
from authentication.models import User 
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from .models import User

class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','role']

class Registerserilaizer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=120,min_length=6,write_only=True)
    class Meta:
        model = User
        fields = ('firstname','lastname','password','id',)
    def update(self, instance, validated_data):
        instance.firstname = validated_data.pop('firstname', instance.firstname)
        instance.lastname = validated_data.pop('lastname', instance.lastname)
        instance.set_password(validated_data.pop('password'))
        instance.save()
        return instance

class UserAssginedToProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','email',)

class userSerializer(serializers.ModelSerializer): 
    class Meta:
        model = User
        fields =('id','firstname','email', 'lastname','role', )  

class LoginSerializer(serializers.ModelSerializer): 
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68,min_length=6,write_only=True)
    firstname=serializers.CharField(max_length=68,min_length=6,read_only=True)
    lastname=serializers.CharField(max_length=68,min_length=6,read_only=True)
    tokens=serializers.SerializerMethodField()
    
    
    # user_profile = User.objects.get(user=request.user)
    # context = {'user_profile': user_profile}
    
    def get_tokens(self,obj):
        # 1/ get the real user from obj
        user =User.objects.get(email=obj['email'])
        return{
            'token' :user.tokens(),
          #  'access':user.tokens()['access'],
          #  'refresh':user.tokens()['refresh'], 
 
        }
    class Meta: 
        model =User 
        fields=['id','firstname','lastname','email','role','password','ttamount','dayoffamount','tokens','token',]
        read_only_fields =['token']
    
    def validate(self,attrs):
        email=attrs.get('email','')
        password=attrs.get('password','')
        
        user=auth.authenticate(email=email,password=password)

        if not user :
            raise AuthenticationFailed('Invalid credentials, try again ')
        """  if not user.is_active :
            raise AuthenticationFailed('Account disabled , contact admin ')
        if not user.is_verified :
            raise AuthenticationFailed('Email is not verified ')    
         """
        return{
            'id':user.id,
            'role':user.role,
            'email': user.email,
            'tel':user.tel,
            'position':user.position,
            'lastname': user.lastname,
            'firstname': user.firstname,
            'ttamount':user.ttamount,
            'dayoffamount':user.dayoffamount,
            'tokens': user.tokens(),
            'token' :user.token
        }


        return super().validate(attrs)


class LogoutSerializer(serializers.Serializer): 
    refresh=serializers.CharField()
    default_error_messages ={
        'bad_token':('Token is expired or invalid')
    }
    def validate(self, attrs):
       self.token=attrs['refresh']
       return attrs

    def save(self,**kwargs):
        try:
         RefreshToken(self.token).blacklist()
        except TokenError :
            self.fail('bad_token')

class UpdateUserSerilaizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['id','firstname','lastname','email','role']
        def update(self, instance, validated_data):
            instance.firstname = validated_data.pop('firstname', instance.firstname)
            instance.lastname = validated_data.pop('lastname', instance.lastname)
            instance.email = validated_data.pop('email', instance.email)
            instance.role = validated_data.pop('role', instance.role)

            instance.save()
            return instance
        
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255, min_length=3)

    def validate_email(self, value):
        # Check if the provided email exists in your database
        # You can add custom logic here to validate the email
        # and ensure it belongs to an existing user.
        return value
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_photo']