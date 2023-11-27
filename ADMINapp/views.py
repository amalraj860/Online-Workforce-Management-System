from django.shortcuts import render,redirect
from .models import admin_signup
from jobseekerapp.models import class_applicant_signup,application_form
from HRapp.models import company_signup,job_posting


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


def admin_jobseeker_home_fn(requests):
    if 'admin_id' in requests.session:
        id1 = requests.session['admin_id']
        data1 = admin_signup.objects.filter(admin_email=id1)
        for x in data1:
            a = x.admin_name
        print(a)
        print(id1)
        return render(requests, 'admin_jobseeker_home.html', {'data1': a})
    else:
        return render(requests, 'admin_login.html')


def admin_hr_home_fn(requests):
    if 'admin_id' in requests.session:
        id1 = requests.session['admin_id']
        data1 = admin_signup.objects.filter(admin_email=id1)
        for x in data1:
            a = x.admin_name
        print(a)
        print(id1)
        return render(requests, 'admin_hr_home.html', {'data1': a})
    else:
        return render(requests, 'admin_login.html')

def admin_jobseeker_add_fn(requests):
    if requests.method == "POST":
        applicant_name = requests.POST.get("name")
        applicant_address = requests.POST.get("address")
        applicant_city = requests.POST.get("city")
        applicant_email = requests.POST.get("email")
        applicant_contact = requests.POST.get("contactnumber")
        applicant_psw = requests.POST.get("psw")
        applicant_signup = class_applicant_signup()
        applicant_signup.name = applicant_name
        applicant_signup.address = applicant_address
        applicant_signup.city = applicant_city
        applicant_signup.email = applicant_email
        applicant_signup.contact = applicant_contact
        applicant_signup.password = applicant_psw
        applicant_signup.save()
        return redirect('/')
    return render (requests,"admin_jobseeker_signup.html")


def admin_hr_add_fn(requests):
    if requests.method == "POST":
        company_name1 = requests.POST.get("companyname")
        company_address1 = requests.POST.get("companyaddress")
        company_email1 = requests.POST.get("companyemail")
        company_contact1 = requests.POST.get("companycontactnumber")
        company_password1 = requests.POST.get("psw")
        company_sign_up = company_signup()
        company_sign_up.company_name = company_name1
        company_sign_up.company_address = company_address1
        company_sign_up.company_email = company_email1
        company_sign_up.company_contact = company_contact1
        company_sign_up.company_password = company_password1
        company_sign_up.save()
        return redirect('/login')

    return render(requests, "admin_hr_signup.html")

def admin_jobseeker_show_fn(requests):
    if 'admin_id' in requests.session:
        id1 = requests.session['admin_id']
        data1 = admin_signup.objects.filter(admin_email=id1)
        for x in data1:
            a = x.admin_name
        print(a)
        print(id1)
        candidates_details = class_applicant_signup.objects.all()
        return render(requests, 'admin_jobseeker_show.html',{'candidate':candidates_details})
    else:
        return render(requests, 'admin_login.html')

def admin_hr_show_fn(requests):
    if 'admin_id' in requests.session:
        id1 = requests.session['admin_id']
        data1 = admin_signup.objects.filter(admin_email=id1)
        for x in data1:
            a = x.admin_name
        print(a)
        print(id1)
        hr_details = company_signup.objects.all()
        return render(requests, 'admin_hr_show.html',{'hr':hr_details})
    else:
        return render(requests, 'admin_login.html')



def admin_jobseeker_update_fn(requests,id):
    print("Bla b laaaa")
    edit = class_applicant_signup.objects.filter(id=id)
    if 'admin_id' in requests.session:
        id1 = requests.session['admin_id']
        data1 = admin_signup.objects.filter(admin_email=id1)
        for x in data1:
            a = x.admin_name
        print(a)
        print(id1)
        if requests.method == "POST":
            applicant_info = class_applicant_signup.objects.get(id=id)
            applicant_info.name = requests.POST.get("name")
            applicant_info.address = requests.POST.get("address")
            applicant_info.city = requests.POST.get("city")
            applicant_info.email = requests.POST.get("email")
            applicant_info.contact = requests.POST.get("contactnumber")
            applicant_info.password = requests.POST.get("psw")
            applicant_info.save()
        return render(requests, 'admin_update_jobseeker.html', {'applicant_updates': edit})
    else:
        return redirect('/login')

def admin_hr_update_fn(requests,id):
    edit = company_signup.objects.filter(id=id)
    print(edit)
    if 'admin_id' in requests.session:
        id1 = requests.session['admin_id']
        data1 = admin_signup.objects.filter(admin_email=id1)
        for x in data1:
            a = x.admin_name
        print(a)
        print(id1)
        if requests.method == "POST":
            company_info = company_signup.objects.get(id=id)
            company_info.company_name = requests.POST.get("companyname")
            company_info.company_address = requests.POST.get("companyaddress")
            company_info.company_email = requests.POST.get("companyemail")
            company_info.company_contact = requests.POST.get("companycontactnumber")
            company_info.company_password = requests.POST.get("psw")
            company_info.save()
        return render(requests, 'admin_update_hr.html', {'hr_updates': edit})
    else:
        return redirect('/login')


def admin_jobseeker_jobview_fn(requests,id):
    print(id)
    user_data = class_applicant_signup.objects.get(id=id)
    data_user = class_applicant_signup.objects.filter(id=int(id))

    if 'admin_id' in requests.session:
        id1 = requests.session['admin_id']
        data1 = admin_signup.objects.filter(admin_email=id1)
        for x in data1:
            a = x.admin_name
        print(a)
        print(id1)
        application_data1 = application_form.objects.filter(applicant_id=user_data)
        print(application_data1)
        return render(requests,'admin_jobseeker_jobview.html',{"application_data":application_data1,"applicant":data_user})




def admin_jobseeker_delete_fn(requests,id):
    candidate_dtl=class_applicant_signup.objects.get(id=id)
    candidate_dtl.delete()
    return redirect("/super_user/show")




def admin_logout(requests):
    try:
        del requests.session['admin_id']
        return redirect('/')
    except:
        return redirect('/')