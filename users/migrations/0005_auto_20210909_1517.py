# Generated by Django 3.2.7 on 2021-09-09 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_pusblisher_pusblishercategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='PusblisherCategoryEnglish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PusblisherCategoryfranch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='PusblisherCategory',
            new_name='PusblisherCategoryArabic',
        ),
        migrations.RenameField(
            model_name='pusblisher',
            old_name='category',
            new_name='category_ar',
        ),
        migrations.AddField(
            model_name='pusblisher',
            name='category_en',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.pusblishercategoryenglish'),
        ),
        migrations.AddField(
            model_name='pusblisher',
            name='category_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.pusblishercategoryfranch'),
        ),
    ]