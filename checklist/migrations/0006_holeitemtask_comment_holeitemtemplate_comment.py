# Generated by Django 5.0.6 on 2024-05-22 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0005_alter_productlistshift_role_alter_tasklistshift_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holeitemtask',
            name='comment',
            field=models.TextField(default='', verbose_name='למה לא בוצע'),
        ),
        migrations.AddField(
            model_name='holeitemtemplate',
            name='comment',
            field=models.TextField(default='', verbose_name='למה לא בוצע'),
        ),
    ]
