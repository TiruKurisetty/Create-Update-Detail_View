# Generated by Django 4.2.2 on 2023-08-07 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scname', models.CharField(max_length=100)),
                ('scprincipal', models.CharField(max_length=100)),
                ('sclocation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=100)),
                ('sage', models.IntegerField()),
                ('scname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.school')),
            ],
        ),
    ]
