# Generated by Django 2.2.1 on 2020-07-14 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0017_remove_attempt_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='attempt',
            name='attempt_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
