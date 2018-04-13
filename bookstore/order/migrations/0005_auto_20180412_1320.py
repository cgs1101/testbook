# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20180412_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.SmallIntegerField(choices=[(5, '已完成'), (1, '待支付'), (2, '待发货'), (3, '待收货'), (4, '待评价')], default=1, verbose_name='订单状态'),
        ),
    ]
