# Generated by Django 5.0.6 on 2024-05-14 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theID', '0019_voyage_yesno_scenario_norgreg_zone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='crew_experience',
            field=models.IntegerField(choices=[(0, 'Low'), (1, 'High')], default=0),
        ),
    ]
