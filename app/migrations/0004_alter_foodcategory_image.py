# Generated by Django 4.2.4 on 2023-08-15 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_foodcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcategory',
            name='image',
            field=models.ImageField(blank=True, upload_to='services'),
        ),
    ]
