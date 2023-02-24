# Generated by Django 4.1.7 on 2023-02-23 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("my_services", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(model_name="bank", old_name="Image", new_name="image",),
        migrations.AlterField(
            model_name="bank",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="bank",
            name="telephone",
            field=models.CharField(blank=True, max_length=25, null=True),
        ),
    ]
