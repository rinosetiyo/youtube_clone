# Generated by Django 5.1.4 on 2025-01-01 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubeClone', '0004_video_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='youtubeClone.video'),
        ),
    ]
