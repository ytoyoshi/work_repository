# Generated by Django 4.2.2 on 2023-07-03 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0003_todomodel_complete"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todomodel",
            name="priority",
            field=models.CharField(
                choices=[("1", "High"), ("2", "Medium"), ("3", "Low")],
                default="2",
                max_length=1,
            ),
        ),
    ]
