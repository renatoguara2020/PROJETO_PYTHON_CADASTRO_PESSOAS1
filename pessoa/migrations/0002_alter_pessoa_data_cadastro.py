# Generated by Django 4.1.1 on 2022-10-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pessoa", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pessoa",
            name="data_cadastro",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
