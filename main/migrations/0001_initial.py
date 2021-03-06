# Generated by Django 3.2.9 on 2021-11-02 04:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=200)),
                ('post_content', models.TextField()),
                ('date_posted', models.DateTimeField(verbose_name='date posted')),
            ],
        ),
    ]
