# Generated by Django 4.2.4 on 2023-08-15 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='phone_number',
            field=models.CharField(default='exit', max_length=14),
            preserve_default=False,
        ),
    ]