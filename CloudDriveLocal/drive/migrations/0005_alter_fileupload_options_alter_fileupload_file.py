# Generated by Django 5.1.1 on 2024-10-12 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("drive", "0004_alter_fileupload_options_alter_fileupload_file"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="fileupload",
            options={},
        ),
        migrations.AlterField(
            model_name="fileupload",
            name="file",
            field=models.FileField(upload_to="uploads/"),
        ),
    ]
