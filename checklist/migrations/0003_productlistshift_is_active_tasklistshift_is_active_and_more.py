# Generated by Django 5.0.6 on 2024-05-22 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_alter_holeitemtask_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlistshift',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is_active'),
        ),
        migrations.AddField(
            model_name='tasklistshift',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is_active'),
        ),
        migrations.AddField(
            model_name='templateproductlistshift',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is_active'),
        ),
        migrations.AddField(
            model_name='templatetasklistshift',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='is_active'),
        ),
        migrations.AlterField(
            model_name='holeitemtask',
            name='status',
            field=models.CharField(choices=[('done', 'בוצע'), ('not_done', 'לא בוצע'), ('choose', 'נא לבחור')], max_length=40, verbose_name='סטטוס'),
        ),
        migrations.AlterField(
            model_name='holeitemtemplate',
            name='status',
            field=models.CharField(choices=[('done', 'בוצע'), ('not_done', 'לא בוצע'), ('choose', 'נא לבחור')], max_length=40, verbose_name='סטטוס'),
        ),
        migrations.AlterField(
            model_name='productlistshift',
            name='shift',
            field=models.CharField(choices=[('morning', 'בוקר'), ('evening', 'עֶרֶב')], max_length=30, verbose_name='shift'),
        ),
        migrations.AlterField(
            model_name='productlistshift',
            name='workday',
            field=models.CharField(blank=True, choices=[('working_day', 'יום עבודה'), ('day_off', 'יום חופש')], max_length=30, null=True, verbose_name='is_work_day'),
        ),
        migrations.AlterField(
            model_name='tasklistshift',
            name='shift',
            field=models.CharField(choices=[('morning', 'בוקר'), ('evening', 'עֶרֶב')], max_length=30, verbose_name='shift'),
        ),
        migrations.AlterField(
            model_name='tasklistshift',
            name='workday',
            field=models.CharField(blank=True, choices=[('working_day', 'יום עבודה'), ('day_off', 'יום חופש')], max_length=30, null=True, verbose_name='is_work_day'),
        ),
        migrations.AlterField(
            model_name='templateproductlistshift',
            name='shift',
            field=models.CharField(choices=[('morning', 'בוקר'), ('evening', 'עֶרֶב')], max_length=30, verbose_name='shift'),
        ),
        migrations.AlterField(
            model_name='templateproductlistshift',
            name='workday',
            field=models.CharField(blank=True, choices=[('working_day', 'יום עבודה'), ('day_off', 'יום חופש')], max_length=30, null=True, verbose_name='is_work_day'),
        ),
        migrations.AlterField(
            model_name='templatetasklistshift',
            name='shift',
            field=models.CharField(choices=[('morning', 'בוקר'), ('evening', 'עֶרֶב')], max_length=30, verbose_name='shift'),
        ),
        migrations.AlterField(
            model_name='templatetasklistshift',
            name='workday',
            field=models.CharField(blank=True, choices=[('working_day', 'יום עבודה'), ('day_off', 'יום חופש')], max_length=30, null=True, verbose_name='is_work_day'),
        ),
    ]
