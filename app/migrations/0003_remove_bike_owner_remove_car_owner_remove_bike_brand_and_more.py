# Generated by Django 4.2.6 on 2023-11-08 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_bike_options_alter_brand_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='car',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='bike',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='car',
            name='brand',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='bike',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
        migrations.AddField(
            model_name='car',
            name='brand',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brand'),
        ),
    ]
