# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 16:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import main.models.item


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_shop_tax_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='name',
        ),
        migrations.RemoveField(
            model_name='item',
            name='price',
        ),
        migrations.RemoveField(
            model_name='item',
            name='reference_code',
        ),
        migrations.RemoveField(
            model_name='item',
            name='starred',
        ),
        migrations.RemoveField(
            model_name='item',
            name='times_sold',
        ),
        migrations.RemoveField(
            model_name='item',
            name='visible',
        ),
        migrations.RemoveField(
            model_name='item',
            name='wholesale_price',
        ),
        migrations.AddField(
            model_name='item',
            name='born_date',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha nacimiento'),
        ),
        migrations.AddField(
            model_name='item',
            name='colour',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='item',
            name='familiar_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre familiar'),
        ),
        migrations.AddField(
            model_name='item',
            name='father',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Padre'),
        ),
        migrations.AddField(
            model_name='item',
            name='fourth_image',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to=main.models.item.upload_to),
        ),
        migrations.AddField(
            model_name='item',
            name='mother',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Madre'),
        ),
        migrations.AddField(
            model_name='item',
            name='official_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre oficial'),
        ),
        migrations.AddField(
            model_name='item',
            name='second_image',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to=main.models.item.upload_to),
        ),
        migrations.AddField(
            model_name='item',
            name='sex',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Sexo'),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Tamaño'),
        ),
        migrations.AddField(
            model_name='item',
            name='third_image',
            field=models.ImageField(blank=True, max_length=1000, null=True, upload_to=main.models.item.upload_to),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', related_query_name='item', to='main.Category', verbose_name='Pelo'),
        ),
    ]
