# Generated by Django 4.0.4 on 2022-04-24 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('contact_no', models.CharField(max_length=100)),
                ('qualifications', models.CharField(blank=True, max_length=100, null=True)),
                ('passout_year', models.IntegerField(blank=True, default='', null=True)),
            ],
        ),
    ]
