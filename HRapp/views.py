from django.shortcuts import render, redirect
from .models import company_signup, job_posting


from jobseekerapp.models import application_form
# for dowlload pdf file


from django.http import FileResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.conf import settings
import os


# Create your views here.
# hr sign up
def hr_signup(requests):
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

    return render(requests, "hr_signup.html")


# hr login page
def hr_login(requests):
    print("hr login")
    if requests.method == "POST":
        hr_username = requests.POST.get('usrname')
        hr_password = requests.POST.get('passwrd')
        print(hr_username, hr_password)
        checking = company_signup.objects.filter(company_email=hr_username, company_password=hr_password).values()
        print(checking)
        if checking:
            if company_signup.objects.filter(company_email=hr_username, status="Active").values():
                requests.session['hr_id'] = hr_username
                print("user exists")
                return render(requests, 'hr_home.html')
            else:
                return render(requests, 'main_page.html',{"status":"inactive"})

        else:
            return render(requests, 'main_page.html',{"status":"invalid"})
    return render(requests, 'main_page.html')


# hr home page
def hr_home(requests):
    if 'hr_id' in requests.session:
        id1 = requests.session['hr_id']
        data1 = company_signup.objects.filter(company_email=id1)
        for x in data1:
            a = x.company_name
        print(id1)
        return render(requests, 'hr_home.html', {'data1': a})
    else:
        return render(requests, 'main_page.html')


# hr logout
def hr_logout(requests):
    try:
        del requests.session['hr_id']
        return redirect('/')
    except:
        return redirect('/')


# job posting
def job_posting_fn(requests):
    global ID
    if 'hr_id' in requests.session:
        company_email = requests.session['hr_id']
        data = company_signup.objects.filter(company_email=company_email)
        for x in data:
            a = x.company_name
            ID = x.id
        print(ID)
        print(company_email)
        # jobposting_autofill = company_signup.objects.get(company_email=company_email)
        # print(jobposting_autofill)
        if requests.method == "POST":
            job_title1 = requests.POST.get("jobtitle")
            job_description1 = requests.POST.get("jd")
            job_location1 = requests.POST.get("location")
            job_salary1 = requests.POST.get("salary1")
            job_experience1 = requests.POST.get("exp")
            job_postingdate1 = requests.POST.get("postingdate")
            job_closingdate1 = requests.POST.get("closingdate")
            jobposting = job_posting()
            jobposting.company_id_id = ID
            jobposting.job_title = job_title1
            jobposting.job_description = job_description1
            jobposting.job_location = job_location1
            jobposting.job_salary = job_salary1
            jobposting.job_experience = job_experience1
            jobposting.job_posting_date = job_postingdate1
            jobposting.job_closing = job_closingdate1
            jobposting.save()
            return redirect("home_hr")
        return render(requests, 'jobposting.html', {'data': a})


# HR job post details
def hr_job_history_fn(requests):
    if 'hr_id' in requests.session:
        company_email = requests.session['hr_id']
        data = company_signup.objects.filter(company_email=company_email)
        for x in data:
            a = x.company_name
            Id = x.id
        job_detailed_history = job_posting.objects.filter(company_id_id=Id)
        print(job_detailed_history)
        return render(requests, 'my_post.html', {'my_history': job_detailed_history, 'data1': a})
    else:

        return render(requests, 'main_page.html')


# show the details of  applied candidates

def view_the_applied_candidate_fn(requests, id):
    if 'hr_id' in requests.session:
        company_email = requests.session['hr_id']
        data = company_signup.objects.filter(company_email=company_email)
        jobs = job_posting.objects.all()
        for x in data:
            a = x.company_name
            # Id = x.id
        applicant_job_detailed_history = application_form.objects.filter(job_details_id=id)
        print(applicant_job_detailed_history)
        return render(requests, 'hr_appliedcandidates_details.html',
                      {'applied_job_seeker_history': applicant_job_detailed_history, 'data1': a})
    else:
        return render(requests, 'main_page.html')


# HR profile updation

def hr_profile_updation_fn(requests):
    if 'hr_id' in requests.session:
        company_email = requests.session['hr_id']
        data = company_signup.objects.filter(company_email=company_email)
        for x in data:
            a = x.company_name
            Id = x.id
        if requests.method == "POST":
            company_info = company_signup.objects.get(id=Id)
            company_info.company_name = requests.POST.get("companyname")
            company_info.company_address = requests.POST.get("companyaddress")
            company_info.company_email = requests.POST.get("companyemail")
            company_info.company_contact = requests.POST.get("companycontactnumber")
            company_info.company_password = requests.POST.get("psw")
            company_info.save()
        return render(requests, 'hr__form_updation.html', {'hr_updates': data, 'data1': a})
    else:
        return redirect('/login')


# about page
def hr_about(requests):
    if 'hr_id' in requests.session:
        id2 = requests.session['hr_id']
        data2 = company_signup.objects.filter(company_email=id2)
        for x in data2:
            a = x.company_name
        print(id2)
    return render(requests, 'hr_about.html', {'data2': a})


# contact page
def hr_contactus(requests):
    if 'hr_id' in requests.session:
        id3 = requests.session['hr_id']
        data3 = company_signup.objects.filter(company_email=id3)
        for x in data3:
            a = x.company_name
        print(id3)
    return render(requests, 'hr_contact.html', {'data3': a})


# function for download pdf file
def download_pdf(request, id):
    print("jj")
    print('my file name', id)
    # Path to your PDF file

    pdf_path = os.path.join(settings.MEDIA_ROOT, id)
    data = application_form.objects.filter(id=id)
    for x in data:
        name=x.resume
    print(name)
    pdf_path = f"C:\\Users\\Amal Raj\\Desktop\\Job_portal\\media\\{name}"

    if os.path.exists(pdf_path):
        with open(pdf_path, 'r') as pdf_file:
            print("x")
            response = HttpResponse(name, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="{name}"'
            return response

    else:
        # Handle the case when the PDF file does not exist
        # You can return a 404 response or an appropriate error message.
        return HttpResponse("PDF file not found", status=404)
