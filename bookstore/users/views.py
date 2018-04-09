from django.shortcuts import render,redirect
import re
from django.core.urlresolvers import reverse
from .models import Passport,Address
from django.http import JsonResponse
from utils.decorators import login_required
# Create your views here.
def register(request):
	#显示用户注册页面
	return render(request,'users/register.html')

def register_handle(request):
	#进行用户注册
	#接受数据
	username = request.POST.get('user_name')
	password = request.POST.get('pwd')
	email = request.POST.get('email')
	#进行数据检测
	if not all([username,password,email]):
		return render(request,'users/register.html',{'errmsg':'参数不能为空'})
	#判断邮箱是否合法
	if not re.match(r'^[a-z0-9][\w\.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$',email):
		return render(request,'users/register.html',{'errmsg':'邮箱不合法'})
	#进行业务处理,注册
	passport = Passport.objects.add_one_passport(username=username,password=password,email=email)

	return redirect(reverse('books:index'))

def login(request):
	#显示登录界面
	username = ''
	checked = ''
	context = {
		'username': username,
		'checked': checked,
	}
	return render(request,'users/login.html',context)

def login_check(request):
	#进行用户登录校验
	print('ssssss')
	#1.获取数据
	username = request.POST.get('username')
	password = request.POST.get('password')
	remember = request.POST.get('remember')
	print(username)
	print(password)
	print(remember)
	#2.数据校验
	if not all([username,password]):
		#有数据为空
		return JsonResponse({'res':2})

	#3.进行处理,根据用户名和密码查找帐户信息
	passport = Passport.objects.get_one_passport(username=username,password=password)
	print(passport)
	if passport:
		#用户名密码正确
		#获取session中的url_path
		next_url = request.session.get('url_path',reverse('books:index'))
		jres = JsonResponse({'res':1,'next_url':next_url})

		#判断是否需要记住用户名
		if remember == 'true':
			#记住用户名
			jres.set_cookie('username',username,max_age=7*24*3600)
		else:
			#不要记住密码
			jres.delete_cookie('username')

		#记住用户的登录状态
		request.session['islogin'] = True
		request.session['username'] = username
		request.session['passport_id'] = passport.id
		return jres
	else:
		#用户名或密码错误
		return JsonResponse({'res':0})


def logout(request):
	#用户退出

	#清空用户的session信息
	request.session.flush()
	#跳转到首页
	return redirect(reverse('books:index'))
@login_required
def user(request):
	'''用户中心-信息页'''
	passport_id = request.session.get('passport_id')
	#获取用户的基本信息
	addr = Address.objects.get_default_address(passport_id=passport_id)

	books_li = []
	context = {
		'addr':addr,
		'page':user,
		'books_li':books_li
	}

	return render(request,'users/user_center_info.html',context)
