# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordergoods',
            name='books',
        ),
        migrations.RemoveField(
            model_name='ordergoods',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='addr',
        ),
        migrations.RemoveField(
            model_name='orderinfo',
            name='passport',
        ),
        migrations.DeleteModel(
            name='OrderGoods',
        ),
        migrations.DeleteModel(
            name='OrderInfo',
        ),
    ]
