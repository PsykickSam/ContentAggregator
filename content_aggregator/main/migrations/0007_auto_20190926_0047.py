# Generated by Django 2.2.5 on 2019-09-26 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190926_0046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='website',
            name='updated_at',
            field=models.DateTimeField(null=True),
        ),
    ]
