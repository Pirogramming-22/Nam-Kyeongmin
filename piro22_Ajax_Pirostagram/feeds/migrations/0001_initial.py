# Generated by Django 5.1.5 on 2025-01-20 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=20)),
                ('content', models.CharField(max_length=50)),
                ('like_count', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]
