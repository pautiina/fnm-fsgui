# Generated by Django 4.2.4 on 2023-08-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fsgui", "0013_alter_flowspec_dstcidr"),
    ]

    operations = [
        migrations.AlterField(
            model_name="flowspec",
            name="srccidr",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
