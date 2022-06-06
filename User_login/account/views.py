from django.shortcuts import render
from rest_framework.views import APIView, Response
from .serializers import RegistrationSerializer, LoginSerializers
from django.contrib.auth import get_user_model, authenticate, login, logout

User = get_user_model()


class RegistrationApiView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        data = request.data
        serializer = RegistrationSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        email = serializer.data.get('email')
        password = serializer.data.get('password')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return Response({'Message': 'User added', 'Code': 200})


class LoginApiView(APIView):
    permission_classes = ()
    authentication_classes = ()

    def post(self, request):
        data = request.data
        # print(type(data))
        serializer = LoginSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        print(type(username))
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if not user:
            return Response({'Error': 'Check your email and password', 'Code': 401})
        login(request, user)
        return Response({'Message': 'User Logged in', 'Code': 200})


class LogoutApiView(APIView):
    def get(self, request):
        logout(request)
        return Response({'Message': 'Logged Out', 'Code': 200})


class GetAllUser(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            print(request.user)
            user = User.objects.all()
            serializer = RegistrationSerializer(user, many=True)
            return Response({'users': serializer.data, 'Code': 200})
        return Response({'Error': 'You have to login first', 'Code': 412})
