# Generated by Django 5.1.5 on 2025-02-08 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_booktabel_number_of_guests_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In progress', 'In progress'), ('Completed', 'Completed')], default='Pending', max_length=50),
        ),
    ]
