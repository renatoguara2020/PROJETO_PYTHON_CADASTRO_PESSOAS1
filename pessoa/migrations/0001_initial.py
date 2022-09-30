# Generated by Django 4.1.1 on 2022-09-30 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pessoa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome_completo", models.CharField(max_length=255)),
                ("email", models.EmailField(max_length=255)),
                ("ativo", models.BooleanField(default=True)),
                ("data_nascimento", models.DateField(null=True)),
                ("data_cadastro", models.DateField(auto_now_add=True)),
            ],
        ),
    ]
