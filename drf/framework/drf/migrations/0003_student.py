# Generated by Django 4.1 on 2022-11-12 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0002_transformer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=50)),
                ('std', models.IntegerField()),
                ('section', models.IntegerField()),
            ],
        ),
    ]
