# Generated by Django 3.1 on 2020-09-24 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizApp', '0002_auto_20200923_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='questions_id',
            new_name='question',
        ),
        migrations.RenameField(
            model_name='answer',
            old_name='team_id',
            new_name='team',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_state_id',
            new_name='event_state',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='quiz_id',
            new_name='quiz',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='answer_type_id',
            new_name='answer_type',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='tours_id',
            new_name='tour',
        ),
        migrations.RenameField(
            model_name='stage',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='stage',
            old_name='tour_id',
            new_name='tour',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='event_id',
            new_name='event',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='cost_id',
            new_name='cost',
        ),
        migrations.RenameField(
            model_name='tour',
            old_name='quiz_id',
            new_name='quiz',
        ),
    ]