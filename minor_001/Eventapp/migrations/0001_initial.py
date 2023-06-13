# Generated by Django 2.2.19 on 2023-06-13 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(default='Заголовок', max_length=255, verbose_name='Заголовок (title)')),
                ('site_nav', models.CharField(default='Название ссылки', max_length=255, verbose_name='Название ссылки')),
                ('site_nav_position', models.IntegerField(default=0, verbose_name='Приоритет в навигации (0 - исключить)')),
                ('site_content', models.TextField(default='<a id="top_of _page" href="#h1" class="card-link">На раздел 1</a><h6 class="card-subtitle mb-2 text-body-secondary "><a id="h1">Раздел 1</a></h6> <p class="card-text">Содержание раздела 1</p><img src="/static/images/settings_django.png"  height="30px"><a href="#top_of _page" class="card-link">к началу страницы</a>', verbose_name='Основное содержание страницы')),
                ('site_current_date', models.DateTimeField(auto_now=True, verbose_name='Дата Записи')),
            ],
            options={
                'verbose_name': 'Контент текущей страницы',
                'verbose_name_plural': 'Уникальный контент страниц',
                'ordering': ('-site_nav_position',),
            },
        ),
    ]
