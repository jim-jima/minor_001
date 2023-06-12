# Generated by Django 2.2.19 on 2023-06-12 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Exchangeapp', '0002_auto_20230611_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangemodel',
            name='by_10',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exchangemodel',
            name='by_100',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exchangemodel',
            name='by_2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exchangemodel',
            name='by_500',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='exchangemodel',
            name='remainder',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='exchangemodel',
            name='money',
            field=models.IntegerField(default=0, help_text='Введите денежную сумму, а мы придумаем, как её разменять!'),
        ),
    ]
