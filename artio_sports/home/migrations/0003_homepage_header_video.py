# Generated by Django 5.1.3 on 2024-11-12 17:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
        ('wagtailvideos', '0015_video_height_video_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='header_video',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailvideos.video'),
        ),
    ]