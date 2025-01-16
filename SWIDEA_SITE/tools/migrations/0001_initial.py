# Generated by Django 5.1.4 on 2025-01-15 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tool',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='이름')),
                ('type', models.CharField(max_length=20, verbose_name='종류')),
                ('explain', models.TextField(verbose_name='개발툴 설명')),
            ],
        ),
    ]
