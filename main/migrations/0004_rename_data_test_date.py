# Generated by Django 5.0 on 2023-12-16 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_test_views'),
    ]

    operations = [
        migrations.RenameField(
            model_name='test',
            old_name='data',
            new_name='date',
        ),
    ]
