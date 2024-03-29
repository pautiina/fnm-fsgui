# Generated by Django 4.2.4 on 2023-08-23 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fsgui", "0006_alter_flowspec_icmpcode_alter_flowspec_icmptype_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="flowspec", name="icmpcode",),
        migrations.RemoveField(model_name="flowspec", name="icmptype",),
        migrations.RemoveField(model_name="flowspec", name="ipversion",),
        migrations.RemoveField(model_name="flowspec", name="packetlength",),
        migrations.AddField(
            model_name="network",
            name="ipversion",
            field=models.CharField(default="ipv4", max_length=4),
        ),
        migrations.AlterField(
            model_name="flowspec", name="dstip", field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="flowspec", name="dstprt", field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="flowspec", name="name", field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="flowspec",
            name="srcip",
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name="flowspec",
            name="srcprt",
            field=models.CharField(blank=True, max_length=5),
        ),
        migrations.AlterField(
            model_name="network", name="cidr", field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name="network", name="net", field=models.CharField(max_length=50),
        ),
    ]
