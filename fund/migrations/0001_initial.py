# Generated by Django 5.0.3 on 2024-03-05 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('strategy', models.CharField(max_length=50)),
                ('aum', models.IntegerField(blank=True, null=True)),
                ('inception_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Funds',
                'db_table': 'fund',
                'ordering': ['name'],
            },
        ),
    ]