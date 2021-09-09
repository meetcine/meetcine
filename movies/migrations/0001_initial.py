# Generated by Django 3.2.6 on 2021-09-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200)),
                ('original_title', models.CharField(blank=True, max_length=200, null=True)),
                ('info', models.URLField()),
                ('script', models.TextField()),
                ('video', models.URLField()),
                ('qvlink_1', models.URLField()),
                ('qvlink_2', models.URLField()),
                ('qvlink_3', models.URLField()),
                ('qvlink_4', models.URLField()),
                ('twitter', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
