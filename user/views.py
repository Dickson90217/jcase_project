from django.shortcuts import redirect,render
from .models import City
from django.contrib.auth import login,authenticate
# Create your views here.


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username'] #request.POST.get('username')
        password = request.POST['password']
        print(username,password)
    try:
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('case')
        else:
            print('登入失敗')
    except Exception as e:
        print(e)
    return render(request,'./user/login.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')