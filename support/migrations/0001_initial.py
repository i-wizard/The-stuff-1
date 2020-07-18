# Generated by Django 2.2.1 on 2019-07-12 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Support',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(error_messages={'blank': 'Please enter fullname.', 'required': 'Please enter your fullname'}, max_length=120)),
                ('email', models.CharField(error_messages={'blank': 'Please enter your email address', 'required': 'Please enter your email address'}, max_length=120)),
                ('title', models.CharField(error_messages={'blank': 'Please enter title.', 'required': 'Please enter title'}, max_length=1000)),
                ('message', models.TextField(error_messages={'blank': 'Please state your issue', 'required': 'Please state your issue'})),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
    ]
