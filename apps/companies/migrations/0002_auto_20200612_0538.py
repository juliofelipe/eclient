# Generated by Django 3.0.6 on 2020-06-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='name',
            field=models.CharField(help_text='Company Name', max_length=100),
        ),
    ]
