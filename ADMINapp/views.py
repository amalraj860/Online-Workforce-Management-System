from django.shortcuts import render,redirect
from .models import admin_signup

# Create your views here.
def admin_login_fn(requests):
    if requests.method == "POST":
        admin_username = requests.POST.get('username')
        admin_password = requests.POST.get('password')
        print(admin_username, admin_password)
        checking = admin_signup.objects.filter(admin_email=admin_username, admin_password=admin_password).values()
        print(checking)
        if checking:
            requests.session['admin_id'] = admin_username
            print("user exists")
            return render(requests, 'admin_home.html')

        else:
            print("user not exists")
    return render(requests,'admin_login.html')


def admin_home_fn(requests):
    if 'admin_id' in requests.session:
        id1 = requests.session['admin_id']
        data1 = admin_signup.objects.filter(admin_email=id1)
        for x in data1:
            a = x.admin_name
        print(a)
        print(id1)
        return render(requests, 'admin_home.html', {'data1': a})
    else:
        return render(requests, 'admin_login.html')

def admin_logout(requests):
    try:
        del requests.session['admin_id']
        return redirect('/')
    except:
        return redirect('/')