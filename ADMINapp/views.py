from django.db.models import Count
from django.shortcuts import render,redirect
from .models import admin_signup
from jobseekerapp.models import class_applicant_signup,application_form
from HRapp.models import company_signup,job_posting
from datetime import date
from json import dumps
import matplotlib.pyplot as plt


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
        return render(requests, 'admin_jobseeker_home.html')
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
        return render(requests, "admin_hr_home.html")

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
        print(hr_details)
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
            # applicant_info.name = requests.POST.get("name")
            # applicant_info.email = requests.POST.get("email")
            # applicant_info.contact = requests.POST.get("contactnumber")
            applicant_info.status = requests.POST.get("status")
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
            company_info.status = requests.POST.get("status")
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
        return render(requests,'admin_jobseeker_jobview.html',{"application_data":application_data1,"applicant": data_user})


def admin_hr_jobposting_details_fn(requests,id):
    hr_data = company_signup.objects.get(id=id)
    hr_name = company_signup.objects.filter(id=int(id))
    print("hello")

    if 'admin_id' in requests.session:
        id1 = requests.session['admin_id']
        data1 = admin_signup.objects.filter(admin_email=id1)
        for x in data1:
            a = x.admin_name
        print(a)
        print(id1)
    hr_jobs_data = job_posting.objects.filter(company_id=hr_data)
    return render(requests,'admin_hr_jobposting_details.html',{"hr_jobs": hr_jobs_data,"recruiter": hr_name})


def admin_hr_job_candidate_details_fn(requests,id):
    print(id)
    print("ith enth myr")
    job_posting_id = job_posting.objects.get(id=id)
    if 'admin_id' in requests.session:
        id1 = requests.session['admin_id']
        data1 = admin_signup.objects.filter(admin_email=id1)
        for x in data1:
            a = x.admin_name
        print(a)
        print(id1)
    applicant_job_detailed_history = application_form.objects.filter(job_details_id=job_posting_id)
    return render(requests, 'admin_applied_candidate.html', {"applicants": applicant_job_detailed_history})



def admin_jobseeker_delete_fn(requests,id):
    candidate_dtl=class_applicant_signup.objects.get(id=id)
    candidate_dtl.delete()
    return redirect("/super_user/show")

def admin_hr_delete_fn(requests,id):
    hr_dtl = company_signup.objects.get(id=id)
    hr_dtl.delete()
    return redirect("/super_user/hr_show")


#function for finding total number of jobseeker
def admin_jobseeker_count_fn(requests):
    total_count_of_candidates = class_applicant_signup.objects.count()
    total_count_of_recruiters = company_signup.objects.count()
    total_job_notification_published = job_posting.objects.count()
    today = date.today()
    active_jobs_count = job_posting.objects.filter(job_closing__gte=today).count()
    # Get the count of jobs posted by each company
    jobs_count_per_company = job_posting.objects.values('company_id__company_name').annotate(job_count=Count('id'))
    # Extract company names and job counts
    company_names = [entry['company_id__company_name'] for entry in jobs_count_per_company]
    print(company_names)
    job_counts = [entry['job_count'] for entry in jobs_count_per_company]
    print(job_counts)
    # Pass data to the template
    context1 = {
        'company_names': company_names,
        'job_counts': job_counts,
    }
    data_json = dumps(context1)

    return render(requests, "admin_dashboard.html",{"job_seeker_count":total_count_of_candidates, "recruiter_count": total_count_of_recruiters, "job_openings": total_job_notification_published, "current_jobs":active_jobs_count ,"job_count_of_each_company": jobs_count_per_company, "context": context1,"data":data_json})



def admin_logout(requests):
    try:
        del requests.session['admin_id']
        return redirect('/')
    except:
        return redirect('/')