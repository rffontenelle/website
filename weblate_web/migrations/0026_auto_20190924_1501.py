# Generated by Django 2.2.5 on 2019-09-24 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("weblate_web", "0025_auto_20190923_1728")]

    operations = [
        migrations.CreateModel(
            name="Package",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, unique=True)),
                ("verbose", models.CharField(max_length=400)),
                ("price", models.IntegerField()),
                ("limit_languages", models.IntegerField(default=0)),
                ("limit_source_strings", models.IntegerField(default=0)),
                ("backup", models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name="subscription",
            name="package",
            field=models.CharField(max_length=150),
        ),
    ]
