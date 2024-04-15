from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def register_view(request):
    if request.method == "POST":
        # 필드에서 데이터 가져오기
        username = request.POST["username"]
        password = request.POST["password1"]  # 변경됨: "password" -> "password1"
        email = request.POST.get("email", "")

        # 필수 필드 유효성 검사
        if not (username and password):
            return HttpResponse("이름과 패스워드는 필수입니다.")

        # 유저 이름과 이메일 중복 검사
        if User.objects.filter(username=username).exists():
            return HttpResponse("유저이름이 이미 있습니다.")
        if email and User.objects.filter(email=email).exists():
            return HttpResponse("이메일이 이미 있습니다.")

        # 유저 생성 및 로그인
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return redirect('/')
    else:
        return render(request, "accounts/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "accounts/login.html")
    else:
        return render(request, "accounts/login.html")


def logout_view(request):
    logout(request)
    return redirect("/")
