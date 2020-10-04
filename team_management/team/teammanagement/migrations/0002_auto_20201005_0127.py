# Generated by Django 3.1.2 on 2020-10-04 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teammanagement', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_type',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Admin'), (2, 'Regular')], default='1', null=True),
        ),
    ]
