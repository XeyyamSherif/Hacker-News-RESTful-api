# Generated by Django 3.1.7 on 2021-06-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="upvote",
            field=models.IntegerField(default=0, null=True),
        ),
    ]
