from django.contrib.auth.models import User
from rest_framework import serializers,viewsets
from django.contrib.auth import get_user_model

User=get_user_model()

class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()
    confirm_password = serializers.CharField()

    # def validate_password(self,value):
    #     if len(value) < 8:
    #         raise serializers.ValidationError(
    #             'The password must be greater than 8 characters'
    #         )
    #     return value  

    def validate_email(self,value):
        user=User.objects.filter(email=value).exists()
        if user:
            raise serializers.ValidationError("This email is already in use")
        return value



    def validate(str,attrs):
        if attrs.get('password') != attrs.get('confirm_password'):
            raise serializers.ValidationError({
                'details': "password do not match"
            })
        value=attrs.get('email')
        user=User.objects.filter(email=value).exists()
        if user:
            raise serializers.ValidationError("This email is already in use")


        return super().validate(attrs)
        
    # def save(self):
    #     password=self.validated_data['password']
    #     password2=self.validated_data['password2']
    #     if password != password2:
    #         raise serializers.ValidationError({'Error':'Password doesnt match'})
        
    #     account=User(username=self.validated_data['username'])
    #     account.set_password(password)
    #     account.save()
    #     return account