# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-27 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('fitness', '0015_auto_20161026_2019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workouttracker',
            old_name='weight',
            new_name='assisted_reps',
        ),
        migrations.AddField(
            model_name='cardioworkout',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='workouttracker',
            name='date',
            field=models.DateField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workouttracker',
            name='muscle_group',
            field=models.CharField(choices=[('Chest', 'Chest'), ('Back', 'Back'), ('Shoulders', 'Shoulders'), ('Abs', 'Abs'), ('Legs', 'Legs'), ('Arms', 'Arms')], default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workouttracker',
            name='raw_weight',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workouttracker',
            name='lift_type',
            field=models.CharField(choices=[('Bench Press', 'Bench Press'), ('Chest Fly', 'Chest Fly'), ('Dips Machine Fly', 'Dips Machine Fly'), ('Push-up', 'Push-up'), ('Chin-up', 'Chin-up'), ('Pulldown', 'Pulldown'), ('Pull-up', 'Pull-up'), ('Shoulder Shrug', 'Shoulder Shrug'), ('Shoulder Press', 'Shoulder Press'), ('Biceps Curl', 'Biceps Curl'), ('Chin-up', 'Chin-up'), ('Close-Grip Bench Press', 'Close-Grip Bench Press'), ('Dips', 'Dips'), ('Triceps Extension', 'Triceps Extension'), ('Forearms', 'Forearms'), ('Crunch', 'Crunch'), ('Leg Raise', 'Leg Raise'), ('Russian Twist', 'Russian Twist'), ('Sit-up', 'Sit-up'), ('Deadlift', 'Deadlift')], max_length=25),
        ),
    ]
