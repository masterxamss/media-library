# Generated by Django 5.1.1 on 2024-09-29 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0008_book_description_alter_mediareservations_date_due'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(blank=True, default='', max_length=1000, null=True),
        ),
    ]
