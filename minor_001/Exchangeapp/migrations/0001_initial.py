# Generated by Django 2.2.19 on 2023-06-11 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExchangeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('money', models.IntegerField(help_text='Введите денежную сумму, а мы придумаем, как её разменять!')),
            ],
            options={
                'verbose_name': 'Размен валюты',
            },
        ),
    ]