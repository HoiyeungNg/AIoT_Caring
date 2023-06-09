# Generated by Django 4.1.7 on 2023-03-17 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycare_backend', '0004_bodyinfo_environmentinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('body_status', models.CharField(max_length=10)),
                ('temperature', models.DecimalField(decimal_places=2, max_digits=6)),
                ('environment_status', models.CharField(max_length=10)),
                ('update_time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='BodyInfo',
        ),
        migrations.DeleteModel(
            name='EnvironmentInfo',
        ),
    ]
