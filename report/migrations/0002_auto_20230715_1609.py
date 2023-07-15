# Generated by Django 3.0.8 on 2023-07-15 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='multi_user_price',
            field=models.IntegerField(default=4500),
        ),
        migrations.AddField(
            model_name='report',
            name='quantitative_report',
            field=models.IntegerField(default=1650),
        ),
        migrations.AddField(
            model_name='report',
            name='strategic_report',
            field=models.IntegerField(default=899),
        ),
        migrations.AlterField(
            model_name='report',
            name='corporate_user_price',
            field=models.IntegerField(default=6500),
        ),
        migrations.AlterField(
            model_name='report',
            name='single_user_price',
            field=models.IntegerField(default=3650),
        ),
    ]
