# Generated by Django 4.2.7 on 2024-01-30 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('day4app', '0002_alter_course_att_full_marks_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='choice',
            field=models.CharField(choices=[('Option 1', 'Option 1 Description'), ('Option 2', 'Option 2 Description')], default='Option 1', max_length=20),
        ),
    ]
