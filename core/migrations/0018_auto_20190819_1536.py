# Generated by Django 2.2.1 on 2019-08-19 14:36

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_auto_20190819_1352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamesetting',
            name='num_smart_users',
            field=models.SmallIntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to=utilities.helper.Helper.slider_image_upload),
        ),
    ]
