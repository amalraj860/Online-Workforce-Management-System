from django.db import models


# Create your models here.
class company_signup(models.Model):
    company_name = models.CharField(max_length=50)
    company_address = models.CharField(max_length=100)
    company_email = models.EmailField(max_length=30)
    company_contact = models.CharField(max_length=20)
    company_password = models.CharField(max_length=25)

    class Meta:
        db_table = 'hr_signup'


# job posting
class job_posting(models.Model):
    company_id = models.ForeignKey(company_signup, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=50)
    job_description = models.CharField(max_length=1000)
    job_location = models.CharField(max_length=50)
    job_salary = models.CharField(max_length=50)
    job_experience = models.CharField(max_length=50)
    job_posting_date = models.DateField()
    job_closing = models.DateField()

    class Meta:
        db_table = 'hr_job_posting'

