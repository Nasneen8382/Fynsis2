# Generated by Django 3.2.19 on 2023-09-05 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0094_rename_customr_salescreditnote_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='salescreditnote',
            name='gstin',
            field=models.CharField(default='', max_length=100),
        ),
    ]
