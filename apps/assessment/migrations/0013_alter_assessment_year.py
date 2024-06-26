# Generated by Django 5.0.3 on 2024-03-11 08:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0012_alter_article_options_alter_assessment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='year',
            field=models.PositiveSmallIntegerField(default=2024, max_length=4, validators=[django.core.validators.MinValueValidator(limit_value=1990), django.core.validators.MaxValueValidator(limit_value=2100)]),
        ),
    ]
