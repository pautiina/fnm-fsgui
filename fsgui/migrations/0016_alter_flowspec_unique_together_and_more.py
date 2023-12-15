# Generated by Django 4.2.4 on 2023-08-25 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("fsgui", "0015_alter_network_unique_together_alter_network_net_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="flowspec",
            unique_together={("net", "srcip", "srcprt", "dstip", "dstprt", "protocol")},
        ),
        migrations.RemoveField(model_name="flowspec", name="dstcidr",),
        migrations.RemoveField(model_name="flowspec", name="srccidr",),
    ]