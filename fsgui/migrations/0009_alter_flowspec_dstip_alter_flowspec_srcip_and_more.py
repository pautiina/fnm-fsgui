# Generated by Django 4.2.4 on 2023-08-23 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fsgui", "0008_alter_flowspec_dstip_alter_flowspec_srcip_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flowspec", name="dstip", field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name="flowspec",
            name="srcip",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="network", name="net", field=models.CharField(max_length=50),
        ),
    ]