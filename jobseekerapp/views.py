from django.shortcuts import render, redirect,HttpResponse
from .models import class_applicant_signup, application_form
from HRapp.models import company_signup,job_posting
from django.db.models import Q #import django query set
# from django.http import HttpResponse


# Create your views here.
def display(request):
    return render(request, 'main_page.html')


# # job seeker login page
# def jobseeker_login(requests):
#     if requests.method == "POST":
#         jobseeker_username = requests.POST.get('usrname')
#         jobseeker_password = requests.POST.get('passwrd')
#         print(jobseeker_username,jobseeker_password)
#         check = applicant_signup.objects.filter(email=jobseeker_username,password=jobseeker_password).values()
#         print(check)
#         if check:
#             requests.session['jobseeker_id'] = jobseeker_username
#             print("user exists")
#             return render(requests,
#                           )
#         else:
#             print("user not exists")
#     return render(requests,"main_page.html")




# job seeker signup
def job_seeker_signup(requests):
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
        return redirect('/login')
    return render (requests,"jobseeker_signup.html")



  
         




# job seeker login page
def jobseeker_login(requests):
    if requests.method == "POST":
        if "login_btn" in requests.POST:
            if requests.POST.get("optradio") == "hr":
                hr_username = requests.POST.get('usrname')
                hr_password = requests.POST.get('passwrd')
                print(hr_username, hr_password)
                checking = company_signup.objects.filter(company_email=hr_username,
                                                         company_password=hr_password).values()
                print(checking)
                if checking:
                    requests.session['hr_id'] = hr_username

                    return redirect("hr/")

                else:
                    print("user not exists")
            else:
                jobseeker_username = requests.POST.get('usrname')
                jobseeker_password = requests.POST.get('passwrd')
                print(jobseeker_username, jobseeker_password)
                check = class_applicant_signup.objects.filter(email=jobseeker_username,
                                                              password=jobseeker_password).values()
                print(check)
                if check:
                    requests.session['jobseeker_id'] = jobseeker_username
                    print("user exists")
                    applicant = class_applicant_signup.objects.filter(email=jobseeker_username)
                    for i in applicant:
                        b = i.name
                    return render(requests, 'jobseeker_home.html', {'applicant_name': b})

                else:
                    print("user not exists")
        else:
            print(requests.POST.get("optradio"))
            if requests.POST.get("optradio") == "hr":
                return redirect('hr/signup_hr')

                return  render(requests,"hr_signup.html")
            else:
                return redirect('/signup')
                # return  render(requests,"jobseeker_signup.html")


    return render(requests, "main_page.html")


# job-seeker home page or job listing page
def jobseeker_home(requests):

    global name_applicant
    if 'jobseeker_id' in requests.session:
        id1 = requests.session['jobseeker_id']
        applicant = class_applicant_signup.objects.filter(email=id1)
        for i in applicant:
            name_applicant = i.name
        print(id1)
        return render(requests, 'jobseeker_home.html',{'applicant_name': name_applicant})
    else:
        return redirect('/login')

# Notifications or Job listing table
# def job_listing_fn(requests):
#     if 'jobseeker_id' in requests.session:
#         id1 = requests.session['jobseeker_id']
#         applicant = class_applicant_signup.objects.filter(email=id1)
#         for i in applicant:
#             b = i.name
#             if 'q' in requests.GET:
#                 K = requests.GET['q']
#                 #joblist = job_posting.objects.filter(job_title__icontains=K)
#                 joblist_condition = Q(Q(job_title__icontains=K) | Q(job_location__icontains=K) |Q(job_experience__icontains=K))
#                 joblist = job_posting.objects.filter(joblist_condition)
#             else:
#                 joblist = job_posting.objects.all()
#         return render(requests, 'joblisting.html', {'job_list': joblist, 'applicant_name': b})
#     else:
#         return redirect('/login')

def job_listing_fn(requests):
    if 'jobseeker_id' in requests.session:
        id1 = requests.session['jobseeker_id']
        applicant = class_applicant_signup.objects.filter(email=id1)
        for i in applicant:
            b = i.name
            if 'q' in requests.GET:
                print("q")
                K = requests.GET['q']
                print(K)
                #joblist = job_posting.objects.filter(job_title__icontains=K)
                joblist_condition = Q(Q(job_title__icontains=K) | Q(job_location__icontains=K) |Q(job_experience__icontains=K))
                joblist = job_posting.objects.filter(joblist_condition)
                print(joblist)
            else:
                joblist = job_posting.objects.all()
        return render(requests, 'joblisting.html', {'job_list': joblist, 'applicant_name': b})
    else:
        return redirect('/login')


# job application form
def job_application_form_fn(requests,id):
    if 'jobseeker_id' in requests.session:
        id1 = requests.session['jobseeker_id']

        applicant = class_applicant_signup.objects.filter(email=id1)
        for i in applicant:
            b = i.name
            ID = i.id
        job_id = job_posting.objects.filter(id=id)
        data = application_form.objects.filter(job_details_id=id,applicant_id =ID )

        if data:
            print("helllo")
            return render(requests, 'jobapplication_form.html', {'applicant_name': b,'status':'exist'})
        else:

            for x in job_id:
                f = company_signup.objects.filter(id=x.company_id_id)
                for j in f:
                    h = j.company_name
            print(h)

            print(b)
            print(ID)
            print(id)

            if requests.method == "POST":
                job_experience = requests.POST.get("sellist2")
                cvr_letter = requests.POST.get("coverletter")
                resume1 = requests.FILES["resume"]
                application_form1 = application_form()
                application_form1.applicant_id_id = ID
                application_form1.job_details_id_id = id
                application_form1.experience = job_experience
                application_form1.cover_letter = cvr_letter
                application_form1.resume = resume1
                application_form1.save()
                return redirect("/notifications")
            return render(requests, 'jobapplication_form.html', {'applicant_name': b, 'company_name': h})

    else:
        return redirect('/login')



# Applicant job application history

def application_history_fn(requests):
    if 'jobseeker_id' in requests.session:
        id1 = requests.session['jobseeker_id']
        applicant = class_applicant_signup.objects.filter(email=id1)
        print(applicant)
        for i in applicant:
            b = i.name
            c=i.id
        applicant_details = application_form.objects.filter(applicant_id_id=c)
        print(applicant_details)
        return render(requests, 'my_appplication_history.html', {'applicants': applicant_details, 'applicant_name': b})
    else:
        return redirect('/login')


# job seeker profile updation

def job_seeker_profile_updation_fn(requests):
    if 'jobseeker_id' in requests.session:
        id1 = requests.session['jobseeker_id']
        applicant = class_applicant_signup.objects.filter(email=id1)
        print(applicant)
        for i in applicant:
            a = i.id
            b = i.name
            print(b,a)

        if requests.method == "POST":
            applicant_info = class_applicant_signup.objects.get(id=a)
            applicant_info.name = requests.POST.get("name")
            applicant_info.address = requests.POST.get("address")
            applicant_info.city = requests.POST.get("city")
            applicant_info.email = requests.POST.get("email")
            applicant_info.contact = requests.POST.get("contactnumber")
            applicant_info.password = requests.POST.get("psw")
            applicant_info.save()
        return render(requests, 'job_seeker_update_profile.html',{'applicant_updates':applicant,'applicant_name': b})
    else:
        return redirect('/login')




# job seeker logout
def jobseeker_logout(requests):
    try:
        del requests.session['jobseeker_id']
        return redirect('/')
    except:
        return redirect('/')


    # return redirect('login')
    # del requests.session['jobseeker_id']
    # return redirect('login')

# about page
def about(requests):
    if 'jobseeker_id' in requests.session:
        id1 = requests.session['jobseeker_id']
        applicant = class_applicant_signup.objects.filter(email=id1)
        for i in applicant:
            b = i.name
    return render(requests, 'about.html', {'applicant_name': b})


# contact page
def contactus(requests):
    if 'jobseeker_id' in requests.session:
        id1 = requests.session['jobseeker_id']
        applicant = class_applicant_signup.objects.filter(email=id1)
        for i in applicant:
            b = i.name
    return render(requests, 'contact.html', {'applicant_name': b})

