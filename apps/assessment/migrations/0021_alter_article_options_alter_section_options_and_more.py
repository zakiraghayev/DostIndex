# Generated by Django 5.1.1 on 2024-09-10 08:59

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assessment', '0020_remove_assessmentpoint_external'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['code'], 'verbose_name': 'Başlıca Performans Göstərici (KPI) Bloku', 'verbose_name_plural': 'Başlıca Performans Göstərici (KPI) Blokları'},
        ),
        migrations.AlterModelOptions(
            name='section',
            options={'ordering': ['article__code', 'code'], 'verbose_name': 'Başlıca Performans Göstərici (KPI)', 'verbose_name_plural': 'Başlıca Performans Göstəriciləri (KPI)'},
        ),
        migrations.AlterUniqueTogether(
            name='assessment',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='article',
            name='code',
            field=models.CharField(default='1', max_length=5, verbose_name='Blok nömrəsi'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='center',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assessments', to='assessment.dostcenter', verbose_name='Mərkəz'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='quarter',
            field=models.CharField(choices=[('1', 'I Rüb'), ('2', 'II Rüb'), ('3', 'III Rüb'), ('4', 'IV Rüb')], default='1', max_length=16, verbose_name='Rüb'),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='year',
            field=models.PositiveSmallIntegerField(default=2024, validators=[django.core.validators.MinValueValidator(limit_value=1990), django.core.validators.MaxValueValidator(limit_value=2100)], verbose_name='İl'),
        ),
        migrations.AlterField(
            model_name='assessmentpoint',
            name='assessment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='points', to='assessment.assessment', verbose_name='Anket'),
        ),
        migrations.AlterField(
            model_name='assessmentpoint',
            name='section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='points', to='assessment.section', verbose_name='Başlıca Performans Göstərici (KPI)'),
        ),
        migrations.AlterField(
            model_name='assessmentpoint',
            name='value',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Göstərici dəyəri'),
        ),
        migrations.AlterField(
            model_name='dostcenter',
            name='name',
            field=models.CharField(default='DOST Mərkəzi #1', max_length=128, verbose_name='DOST mərkəzinin adı'),
        ),
        migrations.AlterField(
            model_name='dostkpiresult',
            name='dost_center',
            field=models.CharField(default='Dost Mərkəzi #1', max_length=64, verbose_name='DOST mərkəzinin adı'),
        ),
        migrations.AlterField(
            model_name='dostkpiresult',
            name='period_quarter',
            field=models.CharField(default='I rüb', verbose_name='Rüb'),
        ),
        migrations.AlterField(
            model_name='dostkpiresult',
            name='period_year',
            field=models.PositiveIntegerField(default=2024, verbose_name='İl'),
        ),
        migrations.AlterField(
            model_name='section',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sections', to='assessment.article', verbose_name='Blok adı'),
        ),
        migrations.AlterField(
            model_name='section',
            name='code',
            field=models.CharField(default='1', max_length=5, verbose_name='Blok nömrəsi'),
        ),
        migrations.AlterField(
            model_name='section',
            name='coefficient',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Blok əmsalı'),
        ),
        migrations.AlterField(
            model_name='section',
            name='external',
            field=models.BooleanField(default=False, verbose_name='Xarici'),
        ),
        migrations.AlterField(
            model_name='section',
            name='formula',
            field=models.CharField(choices=[('formula_min_max_min', 'Əmsal * Altmeyar * (Aij - Ajmin)/(Ajmax - Ajmin)'), ('formula_max_min_max', 'Əmsal * Altmeyar * (Aij - Ajmax)/(Ajmin - Ajmax)')], null=True, verbose_name='Düstur'),
        ),
        migrations.AlterField(
            model_name='section',
            name='maximum',
            field=models.FloatField(default=1, help_text='Aj üçün mümkün yuxarı sərhədd', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Yuxarı sərhəd'),
        ),
        migrations.AlterField(
            model_name='section',
            name='minimum',
            field=models.FloatField(default=1, help_text='Aj üçün mümkün aşağı sərhədd', validators=[django.core.validators.MinValueValidator(0)], verbose_name='Aşağı sərhəd'),
        ),
        migrations.AlterField(
            model_name='section',
            name='sub_points',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='İndiqator əmsalı'),
        ),
        migrations.AlterField(
            model_name='section',
            name='title',
            field=models.CharField(default='Hədəfə çatma', max_length=64, verbose_name='Göstərici adı'),
        ),
        migrations.AlterUniqueTogether(
            name='assessment',
            unique_together={('quarter', 'center', 'year')},
        ),
    ]
