# Generated by Django 3.2.16 on 2022-12-04 01:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scorebrowser', '0003_difficulties'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongVisibility',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='SongVisibilityPreference',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('hide_challenge_white', models.BooleanField(default=False)),
                ('hide_challenge_gold', models.BooleanField(default=False)),
                ('gold_visibility', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='gold', to='scorebrowser.songvisibility')),
                ('song', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorebrowser.song')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorebrowser.user')),
                ('white_visibility', models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, related_name='white', to='scorebrowser.songvisibility')),
            ],
        ),
    ]
