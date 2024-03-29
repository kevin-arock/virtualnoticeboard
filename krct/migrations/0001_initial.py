# Generated by Django 4.0.4 on 2023-03-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CtPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('date', models.DateField(null=True)),
                ('time', models.TimeField(blank=True, null=True, unique=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='pics/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
            ],
        ),
    ]
