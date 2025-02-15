# Generated by Django 5.1.1 on 2025-01-19 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0004_remove_customerrequest_approved_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerrequest',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='customer_address',
            field=models.TextField(default='Unkown Address'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='customer_phone',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customerrequest',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')], default='Pending', max_length=50),
        ),
    ]
