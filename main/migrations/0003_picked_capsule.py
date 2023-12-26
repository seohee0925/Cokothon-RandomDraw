# Generated by Django 5.0 on 2023-12-27 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_capsule_email'),
    ]

    operations = [
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