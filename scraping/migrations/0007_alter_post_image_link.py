# Generated by Django 4.1.3 on 2022-11-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0006_alter_post_category_alter_post_image_link_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_link',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
    ]