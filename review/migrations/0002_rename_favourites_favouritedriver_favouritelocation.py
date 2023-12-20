# Generated by Django 4.2.7 on 2023-12-20 02:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('map', '0001_initial'),
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Favourites',
            new_name='FavouriteDriver',
        ),
        migrations.CreateModel(
            name='FavouriteLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_location', to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favourite_location', to='map.locations')),
            ],
        ),
    ]
