# Generated by Django 4.2.6 on 2024-02-28 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0002_complaint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]