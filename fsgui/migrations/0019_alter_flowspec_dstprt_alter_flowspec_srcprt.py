# Generated by Django 4.2.4 on 2023-09-15 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fsgui", "0018_alter_flowspec_dstprt_alter_flowspec_protocol_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flowspec",
            name="dstprt",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="flowspec",
            name="srcprt",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
