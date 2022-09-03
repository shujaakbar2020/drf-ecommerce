from datetime import date
from django.shortcuts import render
from rest_framework.views import APIView
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .utils import get_tokens_for_user
# from users.models import RefreshToken

from users.serializers import RegistrationSerializer



class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # email = request.data['email']
            email = urlsafe_base64_encode(force_bytes(request.data['email']))
            data = {'name': serializer.data['username'], 'email': serializer.data['email'],
                    'link': f"http://110.39.13.199:8000/accounts/verify/{email}/"}
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        if 'email' not in request.data or 'password' not in request.data:
            return Response({'msg': 'Credentials missing'}, status=status.HTTP_400_BAD_REQUEST)
        email = request.data['email']
        password = request.data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            # if user.token_expiry_date >= date.today():
            auth_data = get_tokens_for_user(request.user)
                # refresh_token_db_obj = RefreshToken(
                #     refresh_token=auth_data['refresh'], is_valid=True)
                # refresh_token_db_obj.save()
            return Response({'msg': 'Login Success', **auth_data,}, status=status.HTTP_200_OK)
        return Response({'msg': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'msg': 'Successfully Logged out'}, status=status.HTTP_200_OK)