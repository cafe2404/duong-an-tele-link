# Generated by Django 5.1.3 on 2024-11-27 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='link',
            name='button_text',
            field=models.CharField(default='Bấm vào đây để gặp lễ tân', max_length=255),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(default='Nhắn cho em để set kèo', max_length=255),
        ),
    ]