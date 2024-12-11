# Generated by Django 5.1.3 on 2024-12-02 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserSystemConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_name', models.CharField(help_text="Full OS name (e.g., 'Microsoft Windows 11 Home' or 'Ubuntu 22.04 LTS')", max_length=255)),
                ('os_version', models.CharField(help_text='OS version or kernel version', max_length=255)),
                ('os_config', models.CharField(help_text="System configuration (e.g., 'Standalone Workstation', 'Server', 'Desktop')", max_length=100)),
                ('architecture', models.CharField(choices=[('x86', 'x86'), ('x64', 'x64'), ('ARM', 'ARM')], help_text='System architecture', max_length=20)),
                ('hostname', models.CharField(help_text='System hostname', max_length=255)),
                ('ip_address', models.GenericIPAddressField(blank=True, help_text='System IP address', null=True)),
                ('audit_results_path', models.CharField(max_length=255)),
                ('last_updated', models.DateTimeField(auto_now=True, help_text='Path where audit results are stored')),
            ],
            options={
                'verbose_name': 'System Configuration',
                'verbose_name_plural': 'System Configurations',
            },
        ),
    ]