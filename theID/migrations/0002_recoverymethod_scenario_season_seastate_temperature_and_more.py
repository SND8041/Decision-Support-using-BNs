# Generated by Django 4.0.5 on 2023-03-28 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theID', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecoveryMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Give this scenario a name, please', max_length=50)),
                ('season', models.IntegerField(choices=[(1, 'Winter'), (2, 'Spring'), (3, 'Summer'), (4, 'Fall')], default=3)),
                ('temperature', models.IntegerField(choices=[(1, 'High'), (2, 'Moderate'), (3, 'Low')], default=2)),
                ('sea_state', models.IntegerField(choices=[(1, 'Rough'), (2, 'Calm')], default=1)),
                ('recovery_method', models.IntegerField(choices=[(1, 'MNA'), (2, 'dispersant use'), (3, 'mechanical recovery'), (4, 'in situ burning')], default=1)),
                ('quantity_of_oil', models.IntegerField(help_text='Put quantity of oil in US gallons')),
                ('population_size', models.IntegerField(help_text='The population of the affected community')),
                ('compensation_amount', models.FloatField(help_text='Amount of US dollars in compensation')),
                ('recovery_time', models.FloatField(help_text='recovery time in years')),
                ('rate_of_biodegradation', models.FloatField(default=0.02133, help_text='Rate of biodegradation of spilled oil, a default value is set to 0.02133 mg/Lhr')),
                ('social_discount_rate', models.FloatField(default=0.035, help_text='The social discount rate, a default value is set to 0.035')),
                ('socioeconomic_impact', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='SeaState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Temperature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='ScenarioBuilder',
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
