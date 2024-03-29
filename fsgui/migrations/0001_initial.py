# Generated by Django 4.2.4 on 2023-08-09 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=100, unique=True)),
                ("password", models.CharField(max_length=100)),
                ("name", models.CharField(max_length=1000)),
                ("is_admin", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Network",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("net", models.CharField(max_length=100)),
                ("cidr", models.CharField(max_length=2)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="networks",
                        to="fsgui.user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Flowspec",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=24)),
                ("srcip", models.CharField(max_length=100)),
                ("srccidr", models.CharField(max_length=2)),
                ("dstip", models.CharField(max_length=100)),
                ("dstcidr", models.CharField(max_length=2)),
                ("srcprt", models.CharField(max_length=10)),
                ("dstprt", models.CharField(max_length=10)),
                ("proto", models.CharField(max_length=10)),
                ("ipproto", models.CharField(max_length=10)),
                ("icmptype", models.CharField(max_length=10)),
                ("icmpcode", models.CharField(max_length=10)),
                ("packetlength", models.CharField(max_length=10)),
                ("action", models.CharField(max_length=10)),
                ("active", models.BooleanField(default=False)),
                (
                    "net",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="flowspecs",
                        to="fsgui.network",
                    ),
                ),
            ],
        ),
    ]
