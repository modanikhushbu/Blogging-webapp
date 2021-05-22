from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from blogapp.models import Blog
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,logout,login
import random
from django.http import JsonResponse
# Create your views here.
@login_required()
def Actionhome(request):
    blg_list = Blog.objects.filter(author=request.user)
    return render(request, 'index.html',{'blg_list': blg_list})

def ActionLogincheck(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username ,password =password)
        if user is not None:
              if user.is_active:
                    login(request, user)
                    blg_list = Blog.objects.filter(author=request.user)
                    return render(request, 'index.html',{'blg_list': blg_list})
        else:
            messages.info(request, 'Something went wrong')
            return render(request, 'login.html')
    else:

        return render (request,'login.html')
def ActionSignup(request):
    num1 = random.randrange(1, 50)
    num2 = random.randrange(1, 50)
    global sum
    sum = num1 + num2
    num1 = str(num1)
    num2 = str(num2)
    str_num = "{} + {}".format(num1,num2)
    return render(request, 'registration.html', {"cap": str_num})


def ActionSignupcheck(request):
        if request.method =='POST':
            uname =request.POST['UserName']
            password1=request.POST['password']
            password2=request.POST['confirm_password']
            captcha = request.POST['captcha']
            if sum == int(captcha):
                if password1==password2:
                    if User.objects.filter( username  = uname).exists():
                        messages.info(request,'username taken')
                        return render (request,'registration.html')
                    else:
                        user= User.objects.create_user(username=uname, password=password1)
                        user.save()
                        messages.info(request, 'Account Created')
                        return render(request, 'registration.html')

                else:
                    messages.info(request, 'Password not matching')
                    return render(request, 'registration.html')
            else:
                messages.info(request, "captcha doesn't match")
                return render(request, 'registration.html')

@login_required()
def add_b(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = User.objects.get(username=request.user.username)
        imgfile = request.FILES['file']
        body = request.POST['body']
        visible = request.POST['visible']
        print(visible)
        if visible =='public':
            blog = Blog.objects.create(title=title, visible = True, imgfile = imgfile, body=body,author= author)
            blog.save()
            blg_list = Blog.objects.filter(author=request.user)
            messages.info(request, 'blog posted')
            return render(request, 'index.html',{'blg_list': blg_list})
        else:
            blog = Blog.objects.create(title=title, visible = False, imgfile = imgfile, body=body,author= author)
            blog.save()
            messages.info(request, 'blog posted privately')
            blg_list = Blog.objects.filter(author=request.user)
            return render(request, 'index.html',{'blg_list': blg_list})
    else:
        return render(request,'add_blog.html')

@login_required()
def private_b(request):
    blg_list = Blog.objects.filter(visible =False,author=request.user)
    return render(request, 'private_blogs.html', {'blg_list': blg_list})

@login_required()
def ActionSearch(request):
    query = request.GET['search']
    users= User.objects.filter(username__icontains=query)
    return render(request,'search.html',{'users':users})

@login_required()
def public_b(request,username):
    user = User.objects.get(username=username)
    blg_list = Blog.objects.filter(visible =True,author =user)
    return render(request, 'public_blogs.html', {'blg_list': blg_list,'username': username})