# Generated by Django 4.2.4 on 2023-08-22 14:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fsgui", "0002_alter_network_user_delete_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="flowspec", old_name="ipproto", new_name="ipversion",
        ),
        migrations.RenameField(
            model_name="flowspec", old_name="proto", new_name="protocol",
        ),
    ]
