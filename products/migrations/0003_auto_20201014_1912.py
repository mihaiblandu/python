# Generated by Django 3.0 on 2020-10-14 19:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201012_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feature',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='summary',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='this is cool', null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10000),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]
