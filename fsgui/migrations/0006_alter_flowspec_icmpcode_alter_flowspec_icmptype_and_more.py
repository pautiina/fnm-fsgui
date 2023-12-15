# Generated by Django 4.2.4 on 2023-08-22 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fsgui", "0005_alter_flowspec_icmpcode_alter_flowspec_icmptype_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flowspec",
            name="icmpcode",
            field=models.CharField(blank=True, default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="flowspec",
            name="icmptype",
            field=models.CharField(blank=True, default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="flowspec",
            name="packetlength",
            field=models.CharField(blank=True, default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="flowspec",
            name="protocol",
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="flowspec",
            name="srccidr",
            field=models.CharField(blank=True, max_length=2),
        ),
        migrations.AlterField(
            model_name="flowspec",
            name="srcip",
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name="flowspec",
            name="srcprt",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
