# Generated by Django 5.1.4 on 2025-01-15 07:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0003_alter_idea_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='idea',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='최종 업데이트'),
            preserve_default=False,
        ),
    ]
