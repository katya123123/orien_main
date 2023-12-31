# Generated by Django 4.2.8 on 2023-12-15 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('number', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('message', models.TextField(blank=True, null=True, verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]
