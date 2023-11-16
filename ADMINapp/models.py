from django.db import models

# Create your models here.
class admin_signup(models.Model):
    admin_name = models.CharField(max_length=50)
    company_address = models.CharField(max_length=100)
    admin_email = models.EmailField(max_length=30)
    admin_contact = models.CharField(max_length=20)
    admin_password = models.CharField(max_length=25)

    class Meta:
        db_table = 'admin_signup'

