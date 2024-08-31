# Generated by Django 5.1 on 2024-08-31 02:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("player", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="player",
            name="assists",
        ),
        migrations.RemoveField(
            model_name="player",
            name="blocks",
        ),
        migrations.RemoveField(
            model_name="player",
            name="efficiency",
        ),
        migrations.RemoveField(
            model_name="player",
            name="one",
        ),
        migrations.RemoveField(
            model_name="player",
            name="one_made",
        ),
        migrations.RemoveField(
            model_name="player",
            name="points",
        ),
        migrations.RemoveField(
            model_name="player",
            name="rebounds",
        ),
        migrations.RemoveField(
            model_name="player",
            name="steals",
        ),
        migrations.RemoveField(
            model_name="player",
            name="three",
        ),
        migrations.RemoveField(
            model_name="player",
            name="three_made",
        ),
        migrations.RemoveField(
            model_name="player",
            name="turnover",
        ),
        migrations.RemoveField(
            model_name="player",
            name="two",
        ),
        migrations.RemoveField(
            model_name="player",
            name="two_made",
        ),
        migrations.CreateModel(
            name="Match",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("points", models.IntegerField()),
                ("assists", models.IntegerField()),
                ("rebounds", models.IntegerField()),
                ("steals", models.IntegerField()),
                ("blocks", models.IntegerField()),
                ("turnover", models.IntegerField()),
                ("three", models.IntegerField()),
                ("three_made", models.IntegerField()),
                ("two", models.IntegerField()),
                ("two_made", models.IntegerField()),
                ("one", models.IntegerField()),
                ("one_made", models.IntegerField()),
                ("efficiency", models.IntegerField()),
                ("more_one", models.IntegerField()),
                ("playoff", models.BooleanField(default=False)),
                ("club", models.BooleanField(default=False)),
                ("equipe", models.BooleanField(default=False)),
                ("reguliere", models.BooleanField(default=True)),
                ("ligue_2", models.BooleanField(default=False)),
                ("ligue_1", models.BooleanField(default=False)),
                (
                    "player",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="matches",
                        to="player.player",
                    ),
                ),
            ],
        ),
    ]
