# Generated by Django 3.2.18 on 2023-05-24 10:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='subscript_products',
            field=models.ManyToManyField(related_name='_accounts_user_subscript_products_+', to=settings.AUTH_USER_MODEL),
        ),
    ]
