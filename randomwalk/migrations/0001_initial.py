# Generated by Django 2.2.4 on 2019-08-30 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlackScholes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('price', models.FloatField()),
                ('strike', models.FloatField()),
                ('interest_rate', models.FloatField()),
                ('volatility', models.FloatField()),
                ('time_to_exp', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Black Scholes Model',
            },
        ),
        migrations.CreateModel(
            name='BrownianMotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.FloatField()),
                ('volatility', models.FloatField()),
                ('variance', models.FloatField()),
                ('start', models.FloatField()),
                ('count', models.IntegerField()),
                ('repeat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SampleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('direction', models.IntegerField()),
                ('ip_address', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name_plural': 'Sample Data Model',
                'db_table': 'Sample_Data',
                'ordering': ['created'],
            },
        ),
        migrations.AddIndex(
            model_name='sampledata',
            index=models.Index(fields=['created'], name='created_idx'),
        ),
    ]
