# Generated by Django 5.0 on 2023-12-27 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capsule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('content', models.TextField(verbose_name='내용')),
                ('image', models.ImageField(upload_to='')),
                ('destination', models.CharField(choices=[('unknown', '익명'), ('tome', '나')], max_length=7)),
                ('write_date', models.DateTimeField(auto_now=True)),
                ('open_date', models.CharField(choices=[('minute', '1분 후'), ('month', '1개월 후'), ('3month', '3개월 후'), ('6month', '6개월 후'), ('1year', '1년 후')], max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='picked_capsule',
            fields=[
                ('account_info_email', models.CharField(max_length=100)),
                ('picked_capsule_id', models.AutoField(primary_key=True, serialize=False)),
                ('info_write_date', models.DateField()),
                ('info_open_date', models.DateField()),
                ('info_content', models.TextField()),
                ('info_picture', models.ImageField(upload_to='')),
            ],
        ),
    ]
