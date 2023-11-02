# Generated by Django 4.2.1 on 2023-11-02 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APP', '0003_alter_count_totalcount'),
    ]

    operations = [
        migrations.CreateModel(
            name='breakfastCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCount', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'breakfastCount',
            },
        ),
        migrations.CreateModel(
            name='dinnerCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCount', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'dinnerCount',
            },
        ),
        migrations.CreateModel(
            name='lunchCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCount', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'lunchCount',
            },
        ),
        migrations.CreateModel(
            name='snacksCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalCount', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'snacksCount',
            },
        ),
    ]
