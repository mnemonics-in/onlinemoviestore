# Generated by Django 5.0.1 on 2024-01-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moviename', models.CharField(max_length=20)),
                ('moviedesp', models.CharField(max_length=20)),
                ('movieyear', models.CharField(max_length=20)),
                ('movieimage', models.ImageField(upload_to='movieapp/images')),
            ],
        ),
    ]
