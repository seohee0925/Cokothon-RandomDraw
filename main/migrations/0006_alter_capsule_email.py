# Generated by Django 3.2.21 on 2023-12-27 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_capsule_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capsule',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
