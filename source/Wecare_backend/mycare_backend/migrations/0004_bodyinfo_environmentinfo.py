# Generated by Django 4.1.7 on 2023-03-17 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycare_backend', '0003_account_usergender'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('body_status', models.CharField(max_length=10)),
                ('update_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='EnvironmentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=6)),
                ('environment_status', models.CharField(max_length=10)),
                ('update_time', models.DateTimeField()),
            ],
        ),
    ]
