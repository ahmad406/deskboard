# Generated by Django 3.2.4 on 2021-06-18 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0002_auto_20210618_0946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='Incident_location',
            field=models.CharField(max_length=216),
        ),
        migrations.AlterField(
            model_name='report',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='report',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]