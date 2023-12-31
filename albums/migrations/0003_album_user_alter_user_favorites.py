# Generated by Django 4.2.4 on 2023-08-28 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_user_favorites'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(related_name='fav-users+', to='albums.album'),
        ),
    ]
