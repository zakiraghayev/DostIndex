# Generated by Django 5.0.3 on 2024-03-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0006_alter_dostkpiresult_period_quarter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assessment',
            name='period_end',
        ),
        migrations.RemoveField(
            model_name='assessment',
            name='period_start',
        ),
        migrations.AddField(
            model_name='dostkpiresult',
            name='dost_center',
            field=models.CharField(default='Dost Mərkəzi #1', help_text='Dost mərkəzinin adı', max_length=64),
        ),
    ]