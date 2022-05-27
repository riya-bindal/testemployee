# Generated by Django 4.0.4 on 2022-05-26 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='departments',
            old_name='DepartmentId',
            new_name='department_id',
        ),
        migrations.RenameField(
            model_name='departments',
            old_name='DepartmentName',
            new_name='department_name',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='DateOfJoining',
            new_name='date_of_joining',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='Department',
            new_name='department',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='EmployeeId',
            new_name='employee_id',
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='EmployeeName',
            new_name='employee_name',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='PhotoFileName',
        ),
    ]