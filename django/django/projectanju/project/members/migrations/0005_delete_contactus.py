# Generated by Django 4.2.4 on 2023-10-06 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_rename_newsletter_newslettersubscriber'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ContactUs',
        ),
    ]
