# Generated by Django 4.0.4 on 2023-03-19 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('krce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cepost',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/krce/%m-%y'),
        ),
    ]