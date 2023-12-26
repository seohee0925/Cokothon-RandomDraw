from django.db import models
# from .models import User

class Capsule(models.Model):
    email = models.EmailField()
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(default='media/default_image.jpeg', null=True)
    
    DESTINATION_CHOICES = [
        ("unknown", "익명"),
        ("tome", "나")
    ]

    OPEN_DATE_CHOICES = [
        ("minute", "1분 후"),
        ("month", "1개월 후"),
        ("3month", "3개월 후"),
        ("6month", "6개월 후"),
        ("1year", "1년 후")
    ]
    
    destination = models.CharField(max_length=7, choices=DESTINATION_CHOICES)
    write_date = models.DateTimeField(auto_now=True)
    open_date = models.CharField(max_length=6, choices=OPEN_DATE_CHOICES)

class picked_capsule(models.Model):
    account_info_email = models.CharField(max_length=100)
    picked_capsule_id = models.AutoField(primary_key=True)
    info_write_date = models.DateTimeField()
    info_open_date = models.DateTimeField()
    info_content = models.TextField()
    info_picture = models.ImageField()