# Generated by Django 2.1.1 on 2018-09-17 19:49

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, verbose_name='ISBN')),
                ('first_edition', models.BooleanField()),
                ('type_of_book', models.CharField(choices=[('PB', 'Paperback'), ('HB', 'Hardback')], default='PB', max_length=2)),
            ],
        ),
    ]
