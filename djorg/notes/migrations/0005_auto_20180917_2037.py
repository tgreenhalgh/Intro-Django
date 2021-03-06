# Generated by Django 2.1.1 on 2018-09-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20180917_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='book',
            name='year_published',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn target="_blank" ">ISBN number</a>', max_length=13, verbose_name='ISBN'),
        ),
    ]
