# Generated by Django 2.2.5 on 2019-10-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("weblate_web", "0029_report_version")]

    operations = [
        migrations.AddField(
            model_name="service", name="note", field=models.TextField(blank=True)
        )
    ]
