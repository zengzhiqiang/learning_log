from django.shortcuts import render

from django.shortcuts import redirect

from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.views import auth_logout
# Create your views here.

def logout(request):
    auth_logout(request)
    return redirect('learning_logs:index')

def register(request):
    if request.method != "POST":
        #显示空的注册表单
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #让用户自动登录并重定向到主页
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return redirect('learning_logs:index')
    context = {'form': form}
    return render(request, 'users/register.html', context)