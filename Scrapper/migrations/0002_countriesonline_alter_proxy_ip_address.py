# Generated by Django 5.0.1 on 2024-01-26 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scrapper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountriesOnline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterField(
            model_name='proxy',
            name='ip_address',
            field=models.IntegerField(default=0),
        ),
    ]
