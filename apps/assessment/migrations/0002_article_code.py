# Generated by Django 4.2.10 on 2024-02-28 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='code',
            field=models.CharField(default='1', max_length=5, verbose_name='Kod nömrəsi'),
        ),
    ]
