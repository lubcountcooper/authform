# Generated by Django 2.2 on 2019-04-02 07:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190402_0712'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='API_KEY',
            new_name='api_key',
        ),
    ]
