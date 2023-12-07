# Generated by Django 4.2.4 on 2023-10-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_delete_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('message', models.TextField()),
            ],
        ),
    ]