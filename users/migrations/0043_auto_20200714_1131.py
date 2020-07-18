# Generated by Django 2.2.1 on 2020-07-14 10:31

from django.db import migrations, models
import utilities.helper


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_auto_20200714_1130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_image',
            field=models.ImageField(default='uploads/profile/no-img.png', upload_to=utilities.helper.Helper.user_upload_file_name),
        ),
    ]
