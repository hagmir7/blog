# Generated by Django 4.1.3 on 2023-11-09 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0010_alter_settings_cover_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='Covers'),
        ),
        migrations.AlterField(
            model_name='settings',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='Logos'),
        ),
    ]