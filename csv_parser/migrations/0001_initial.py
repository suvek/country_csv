# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Countrydata',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sr_no', models.IntegerField()),
                ('country_name', models.CharField(max_length=100)),
                ('formal_name', models.CharField(max_length=100)),
                ('country_type', models.CharField(max_length=100)),
                ('country_sub_type', models.CharField(max_length=100)),
                ('sovereignty', models.CharField(max_length=100)),
                ('capital', models.CharField(max_length=100)),
                ('currency_code', models.CharField(max_length=100)),
                ('currency_name', models.CharField(max_length=100)),
                ('telephone_code', models.IntegerField()),
                ('iso_3166_12_letter_code', models.CharField(max_length=100)),
                ('iso_3166_13_letter_code', models.CharField(max_length=100)),
                ('iso_3166_1_number', models.IntegerField()),
                ('iana_country_code_tld', models.CharField(max_length=100)),
            ],
        ),
    ]
