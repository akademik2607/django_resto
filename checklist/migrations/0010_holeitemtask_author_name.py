# Generated by Django 5.0.6 on 2024-05-23 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0009_alter_productlistshift_role_alter_tasklistshift_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holeitemtask',
            name='author_name',
            field=models.CharField(blank=True, max_length=125, null=True, verbose_name='author_name'),
        ),
    ]