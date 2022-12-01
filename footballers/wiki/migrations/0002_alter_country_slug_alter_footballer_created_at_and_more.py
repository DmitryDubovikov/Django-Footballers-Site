# Generated by Django 4.1.3 on 2022-12-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='URL'),
        ),
        migrations.AlterField(
            model_name='footballer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Article created at'),
        ),
        migrations.AlterField(
            model_name='footballer',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='footballer',
            name='published',
            field=models.BooleanField(default=True, null=True, verbose_name='Article published'),
        ),
        migrations.AlterField(
            model_name='footballer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Article updated at'),
        ),
    ]
