# Generated by Django 3.2.7 on 2021-09-19 11:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0022_alter_post_additional_topics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='Additional_Topics',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
