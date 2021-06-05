# Generated by Django 3.0 on 2021-06-05 01:07

from django.db import migrations, models
import users.util


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20210604_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(null=True, upload_to=users.util.UploadFilesReName.rename),
        ),
    ]