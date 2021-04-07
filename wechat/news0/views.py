from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from django.http import HttpResponse


# Create your views here.


class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        """this is the function to log in"""
        print("这个登录包里的数据: ", request.data)
        if request.method == "POST":
            print("开始登录了嗷")
            # 从包里读出相应数据
            thisUserId = request.POST['userid']
            thisUserName = request.POST['username']
            thisUserPlace = request.POST['user_place']
            # User.objects.create(userId=thisUserId, userName=thisUserName, userPlace=thisUserPlace)
            theUsers = User.objects.all()

            print("提交的姓名: ", thisUserName)
            print("提交的id: ", thisUserId)
            print("提交的地址: ", thisUserPlace)
            print("存储的用户: ", theUsers)

            try:
                thisUser = User.objects.get(userId=thisUserId)
                if thisUser.userName != thisUserName:
                    return Response({"what the hell did you just type?"})

            except User.DoesNotExist as e:
                return Response({"notExist"})

            return Response({"status": True})
        else:
            return Response({"status": False})


class SignupView(APIView):

    def post(self, request):
        """this is the function to sign up"""
        print("这个注册包里的数据: ", request.data)
        if request.method == "POST":
            print("开始注册了嗷")
            # 从包里读出响应数据
            thisUserId = request.POST['userid']
            thisUserName = request.POST['username']
            thisUserPlace = request.POST['user_place']

            print("提交的姓名: ", thisUserName)
            print("提交的id: ", thisUserId)
            print("提交的地址: ", thisUserPlace)

            if thisUserId not in User.objects.all():
                return Response({"yep"})

            return Response({"status": True})
        else:
            return Response({"status": False})
