# Generated by Django 5.1.4 on 2025-01-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideas', '0006_alter_idea_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='idea',
            name='created_at',
            field=models.DateTimeField(auto_now=True, verbose_name='최종 업데이트'),
        ),
    ]
