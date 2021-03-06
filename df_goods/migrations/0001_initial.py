# Generated by Django 2.1.2 on 2018-10-23 09:45

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gtitle', models.CharField(max_length=20, verbose_name='商品名称')),
                ('gpic', models.ImageField(upload_to='df_goods', verbose_name='商品图片')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='商品价格')),
                ('isDelete', models.BooleanField(default=False, verbose_name='状态')),
                ('gunit', models.CharField(max_length=20, verbose_name='单位')),
                ('gclick', models.IntegerField(verbose_name='点击量')),
                ('gjianjie', models.CharField(max_length=200, verbose_name='简介')),
                ('gkucun', models.IntegerField(verbose_name='库存')),
                ('gcontent', DjangoUeditor.models.UEditorField(verbose_name='内容')),
            ],
            options={
                'verbose_name': '商品信息',
                'verbose_name_plural': '商品信息',
                'db_table': 'GoodsInfo',
            },
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='df_goods.TypeInfo', verbose_name='类别'),
        ),
    ]
