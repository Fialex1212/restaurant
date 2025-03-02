# Generated by Django 5.1.5 on 2025-02-08 22:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=16, null=True, verbose_name='Phone Number')),
                ('message', models.TextField(blank=True, max_length=121, null=True, verbose_name='Message')),
            ],
        ),
    ]
