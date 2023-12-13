from django.db import models
from HRapp.models import job_posting
from datetime import date

class class_applicant_signup(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    contact = models.CharField(max_length=20)
    password = models.CharField(max_length=25)
    status = models.CharField(max_length=50,null=True,default="Active")

    class Meta:
        db_table = 'job_seeker_details'


# models for application form


class application_form(models.Model):
    applicant_id = models.ForeignKey(class_applicant_signup, on_delete=models.CASCADE)
    job_details_id = models.ForeignKey(job_posting, on_delete=models.CASCADE)
    experience = models.IntegerField()
    cover_letter = models.CharField(max_length=1000)
    resume = models.FileField(null=True)
    date = models.DateField(default=date.today,null=True)

    class Meta:
        db_table = 'job_application_form'


# Download the helper library from https://www.twilio.com/docs/python/install
import os
# from twilio.rest import Client
#
# # Set environment variables for your credentials
# # Read more at http://twil.io/secure
# account_sid = "ACe2069701b9dd71d4b438537bf5116ca5"
# auth_token = "8e5bf1e0873e73d4ed31dbbd5f86a652"
# verify_sid = "VA936e4b82336ea2ac6d8fed8e7ab7cb3f"
# verified_number = "+918606670730"
#
# client = Client(account_sid, auth_token)
#
# verification = client.verify.v2.services(verify_sid) \
#   .verifications \
#   .create(to=verified_number, channel="sms")
# print(verification.status)
#
# otp_code = input("Please enter the OTP:")
#
# verification_check = client.verify.v2.services(verify_sid) \
#   .verification_checks \
#   .create(to=verified_number, code=otp_code)
# print(verification_check.status)