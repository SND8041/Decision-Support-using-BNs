# Generated by Django 4.2.4 on 2023-10-02 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theID', '0013_twooptions_scenario_association_distrupt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scenario',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
