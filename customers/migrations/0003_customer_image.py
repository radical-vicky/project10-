# Generated by Django 5.1.3 on 2024-11-15 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_customer_admissionnumber_customer_phonenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, upload_to='customers_images/'),
        ),
    ]
