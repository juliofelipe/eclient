# Generated by Django 3.0.6 on 2020-06-14 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0004_auto_20200612_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Overtime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=100)),
                ('hours', models.DecimalField(decimal_places=2, max_digits=5)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.Employee')),
            ],
        ),
    ]
