# Generated by Django 4.1.3 on 2022-12-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_alter_country_slug_alter_footballer_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footballer',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Article created at'),
        ),
        migrations.AlterField(
            model_name='footballer',
            name='photo',
            field=models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Photo'),
        ),
        migrations.AlterField(
            model_name='footballer',
            name='published',
            field=models.BooleanField(default=True, verbose_name='Article published'),
        ),
        migrations.AlterField(
            model_name='footballer',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Article updated at'),
        ),
    ]