# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_auto_20180410_0148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.SmallIntegerField(verbose_name='订单状态', choices=[(1, '待支付'), (5, '已完成'), (2, '待发货'), (4, '待评价'), (3, '待收货')], default=1),
        ),
    ]
