# Generated by Django 5.1.4 on 2024-12-31 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_profile'),
        ('youtubeClone', '0004_video_is_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='saved_videos',
            field=models.ManyToManyField(blank=True, null=True, related_name='saved_videos', to='youtubeClone.video'),
        ),
    ]
