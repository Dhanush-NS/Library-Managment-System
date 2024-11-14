# Generated by Django 4.2.3 on 2024-02-25 07:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_alter_book_book_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_add_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='issueditem',
            name='issue_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]