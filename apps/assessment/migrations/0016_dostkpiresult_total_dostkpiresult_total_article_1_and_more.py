# Generated by Django 5.0.3 on 2024-04-01 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0015_alter_section_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='dostkpiresult',
            name='total',
            field=models.FloatField(default=0, help_text='Ümumi'),
        ),
        migrations.AddField(
            model_name='dostkpiresult',
            name='total_article_1',
            field=models.FloatField(default=0, help_text='1. Ümumi - Liderlik'),
        ),
        migrations.AddField(
            model_name='dostkpiresult',
            name='total_article_2',
            field=models.FloatField(default=0, help_text='2. Ümumi - Vətəndaşlar üçün nəticələr'),
        ),
        migrations.AddField(
            model_name='dostkpiresult',
            name='total_article_3',
            field=models.FloatField(default=0, help_text='3. Ümumi - Proseslər üzrə nəticələr'),
        ),
        migrations.AddField(
            model_name='dostkpiresult',
            name='total_article_4',
            field=models.FloatField(default=0, help_text='4. Ümumi - İşçilər üçün nəticələr'),
        ),
        migrations.AddField(
            model_name='dostkpiresultexternal',
            name='total',
            field=models.FloatField(default=0, help_text='Ümumi'),
        ),
    ]
