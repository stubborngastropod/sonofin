# Generated by Django 4.2.1 on 2023-05-23 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="depositproducts",
            name="dcls_month",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
