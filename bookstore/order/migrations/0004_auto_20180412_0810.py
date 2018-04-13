# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20180412_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderinfo',
            name='status',
            field=models.SmallIntegerField(default=1, verbose_name='订单状态', choices=[(1, '待支付'), (4, '待评价'), (2, '待发货'), (5, '已完成'), (3, '待收货')]),
        ),
    ]
