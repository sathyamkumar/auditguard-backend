# Generated by Django 5.1.3 on 2024-12-08 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_usersystemconfig_os_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditresult',
            name='level',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
