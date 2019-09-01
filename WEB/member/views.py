from django.shortcuts import render ,redirect
from django.contrib import auth
from .models import CustomUser
# from django.contrib.auth import login, authenticate
from django.http import HttpResponse
# Create your views here.

#로그인
def login(request):
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = auth.authenticate(request, username = username, password = password)
                if user is not None:
                        auth.login(request, user)
                        return redirect('NawamMa:home')
                else:
                        return HttpResponse('로그인 실패. 다시 시도 하세요')
        else:
                return render(request, 'member/login.html')      

# 로그아웃
def logout(request):
                auth.logout(request)
                return redirect('NawamMa:home')
                
#회원가입
def register(request):
        if request.method == "POST":
                user = CustomUser.objects.create_user( email = request.POST["username"], nickname=request.POST["nickname"], password = request.POST["password"], cellphone = request.POST["phone"], birth = request.POST["birth"],)
                auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('NawamMa:home')
        else:
                return render(request, 'member/register.html')
