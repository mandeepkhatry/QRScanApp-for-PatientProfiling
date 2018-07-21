from django.db import models

# Create your models here.

class Testuser(models.Model):
    user_id = models.CharField(max_length=200)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)