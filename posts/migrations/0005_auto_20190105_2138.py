# Generated by Django 2.1.3 on 2019-01-05 20:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20181231_1156'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='urlImage',
            new_name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(to='categories.Category'),
        ),
    ]
