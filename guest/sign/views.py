
from django.http import HttpResponse
from sign.models import Event,Guest
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# HttpResponseRedirect：构造函数的第一个参数是必要的 — 用来重定向的地址。
def index(request):
    return render(request,"index.html")

# def index(request):
#     return HttpResponse("Hello Django!~~~~我是zqq~~~~")
#     # return HttpResponse( )

# 登录动作  通过 login_aciton 函数来处理登录请求
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 登录
            request.session['user'] = username  # 将session信息记录到浏览器
            response = HttpResponseRedirect('/event_manage/')
            return response
        else:
            return render(request, 'index.html', {'error': 'username or password error!'})

            # if username == 'admin' and password == 'admin123':
        #     response= HttpResponseRedirect('/event_manage/')
        #     response.set_cookie('user', username, 3600)  # 添加浏览器cookie
        #     return response
        # else:
        #     return render(request,'index.html', {'error': 'username or password error!'})
    else:
        return render(request,'index.html', {'error': 'username or password error!'})
# 发布会管理
@login_required
def event_manage(request):
    event_list = Event.objects.all()
    username = request.session.get('user', '')
    return render(request,"event_manage.html",{"user":username, "events":event_list})

# 发布会名称搜索
# @login_required
# def search_name(request):
#     username = request.session.get('user', '')
#     search_name = request.GET.get("name", "")
#     event_list = Event.objects.filter(name__contains=search_name)
#     return render(request, "event_manage.html", {"user": username, "events": event_list})
@login_required
def guest_manage(request):
    username = request.session.get('user', '')
    guest_list = Guest.objects.all()
    return render(request, "guest_manage.html", {"user": username, "guests": guest_list})
