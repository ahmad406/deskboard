# Generated by Django 3.2.4 on 2021-06-17 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=96)),
                ('description', models.CharField(max_length=12)),
                ('date', models.DateField(verbose_name='Date')),
                ('Incident_location', models.CharField(max_length=116)),
                ('Intial_Serverity', models.CharField(max_length=500)),
                ('suspect_cause', models.CharField(max_length=116)),
                ('immediaet_action', models.CharField(max_length=116)),
                ('sub_incident_type', models.CharField(max_length=116)),
            ],
        ),
    ]
