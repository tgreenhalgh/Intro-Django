# Generated by Django 2.1.1 on 2018-09-17 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20180917_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn target="_blank">ISBN number</a>', max_length=13, verbose_name='ISBN'),
        ),
    ]