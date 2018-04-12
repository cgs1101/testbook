# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.SmallIntegerField(default=1, verbose_name='订单状态', choices=[(4, '待评价'), (2, '待发货'), (1, '待支付'), (5, '已完成'), (3, '待收货')]),
        ),
    ]
