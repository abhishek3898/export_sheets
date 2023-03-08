# Generated by Django 4.1.7 on 2023-03-08 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("sheets", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ExcelFileUpload",
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
                ("excel_file_upload", models.FileField(upload_to="excel")),
            ],
        ),
    ]