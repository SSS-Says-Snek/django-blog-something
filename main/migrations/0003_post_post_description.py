# Generated by Django 3.2.9 on 2021-11-02 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_postmodel_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_description',
            field=models.CharField(blank=True, default='', max_length=400),
        ),
    ]