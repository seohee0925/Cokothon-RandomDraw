from django.db import models

# Create your models here.

class picked_capsule(models.Model):
    account_info_email = models.CharField(max_length=100)
    picked_capsule_id = models.AutoField(primary_key=True)
    info_write_date = models.DateField()
    info_open_date = models.DateField()
    info_content = models.TextField()
    info_picture = models.ImageField()