# Generated by Django 3.2 on 2021-09-15 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_auto_20210915_0347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='count',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
