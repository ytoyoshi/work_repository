# Generated by Django 4.2.1 on 2023-07-17 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0006_alter_todomodel_dedline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='dedline',
            new_name='deadline',
        ),
    ]
