# Generated by Django 3.2.16 on 2023-03-18 02:14

from django.db import migrations, models
import django.db.models.deletion
import scorebrowser.models


class Migration(migrations.Migration):

    dependencies = [
        ('scorebrowser', '0033_extra_savior_reorders'),
    ]

    operations = [
        migrations.AddField(
            model_name='cabinet',
            name='gold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='region',
            field=models.ForeignKey(default=scorebrowser.models.default_region, on_delete=django.db.models.deletion.PROTECT, to='scorebrowser.region'),
        ),
    ]
