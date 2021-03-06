# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='permission_census',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='permission_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='team',
            name='system',
            field=models.BooleanField(default=False),
        ),
    ]
