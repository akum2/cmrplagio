# Generated by Django 4.0.4 on 2022-05-14 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='added_on',
            field=models.DateTimeField(auto_now=True, verbose_name='Added Date'),
        ),
    ]
