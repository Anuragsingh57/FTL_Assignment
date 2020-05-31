# Generated by Django 3.0.6 on 2020-05-30 11:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20200530_1633'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityPeriods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activity_periods', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
