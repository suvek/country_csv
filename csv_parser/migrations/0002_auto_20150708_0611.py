# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('csv_parser', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrydata',
            name='iso_3166_1_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='countrydata',
            name='telephone_code',
            field=models.CharField(max_length=100),
        ),
    ]
