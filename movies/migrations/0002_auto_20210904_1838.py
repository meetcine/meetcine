# Generated by Django 3.2.6 on 2021-09-04 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('affects', '0002_remove_affect_def_source'),
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='affect',
            field=models.ManyToManyField(blank=True, to='affects.Affect'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='qvlink_1',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='qvlink_2',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='qvlink_3',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='qvlink_4',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
