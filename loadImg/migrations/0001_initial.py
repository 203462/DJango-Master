# Generated by Django 4.0.1 on 2022-02-08 01:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoadImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_img', models.CharField(max_length=50, null=True)),
                ('url_img', models.ImageField(blank=True, default='', null=True, upload_to='assets/img/')),
                ('format_img', models.CharField(max_length=50, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edited', models.DateTimeField(blank=True, default=None, null=True)),
            ],
        ),
    ]
