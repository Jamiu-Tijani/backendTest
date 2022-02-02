from rest_framework import generics, status
from rest_framework.response import Response
from userReg.models import userData

from userReg.serializers import dataSerializer, weatherSerializer
from userReg.weather_api import get_weather
from rest_framework.response import Response

from userReg.weather_api import get_weather
from userReg.models import userData
from django.db import transaction






class UserReg(generics.GenericAPIView):
    serializer_class = dataSerializer
    @transaction.atomic
    def post(self, request):
        try:
            user=request.data
            username = user['username']
            email = user['email']
            password = user['password']
            image = request.FILES.get('avatar')
            if userData.objects.filter(username = username).exists() or userData.objects.filter(email=email).exists() : # check if email exists
                
                context = {
                'message':'username or email already exists'
                }
                return Response(context)
            else:
                userData.objects.create_user(username, email,password, avatar=image)
                userData.email_user(email, subject="ACCOUNT CREATION", message="account successfully created", from_email= 'jimniz01@gmail.com',)
                userData.save
                context = {
                'message':'user registered successfully'
                }
                return Response(context,status=status.HTTP_201_CREATED)
        except Exception as e:
            error = str(e)

            context = {
                        'message': error,
                    }
            return Response(context)



class getWeather(generics.GenericAPIView):
    serializer_class = weatherSerializer
    def post(self,request):
        try:

            query = request.POST.__getitem__("location")
            result = get_weather(query=query)
            return Response(result, status=status.HTTP_201_CREATED)
        
        
        except Exception as e:
            context = {
                        'message': e
                    }
            return Response(context)



