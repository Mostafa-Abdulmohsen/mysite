# Generated by Django 3.0.7 on 2020-06-10 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200609_1704'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='img',
            field=models.ImageField(default='img', upload_to='img'),
            preserve_default=False,
        ),
    ]
