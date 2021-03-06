# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-02 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20180120_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='entrega',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='entrada',
            name='cor',
            field=models.CharField(blank=True, choices=[('#001F3F', 'NAVY'), ('#3c8dbc', 'AZUL'), ('#00c0ef', 'AZUL-CLARO'), ('#39CCCC', 'TURQUESA'), ('#00a65a', 'VERDE'), ('#605ca8', 'ROXO'), ('#f39c12', 'AMARELO'), ('#ff851b', 'LARANJA'), ('#f56954', 'VERMELHO'), ('#D81B60', 'ROSA'), ('#d2d6de', 'CINZA'), ('#111111', 'PRETO')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='saida',
            name='cor',
            field=models.CharField(blank=True, choices=[('#001F3F', 'NAVY'), ('#3c8dbc', 'AZUL'), ('#00c0ef', 'AZUL-CLARO'), ('#39CCCC', 'TURQUESA'), ('#00a65a', 'VERDE'), ('#605ca8', 'ROXO'), ('#f39c12', 'AMARELO'), ('#ff851b', 'LARANJA'), ('#f56954', 'VERMELHO'), ('#D81B60', 'ROSA'), ('#d2d6de', 'CINZA'), ('#111111', 'PRETO')], max_length=100, null=True),
        ),
    ]
