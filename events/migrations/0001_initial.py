# Generated by Django 4.0.1 on 2022-01-18 10:34

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Event name')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Event date')),
                ('assigner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Assigner')),
            ],
        ),
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Event type')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Request title')),
                ('attachment', models.FileField(blank=True, upload_to='media', verbose_name='Attachment')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.event', verbose_name='Event name')),
                ('participant', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Participant')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='events.eventtype', verbose_name='Event type'),
        ),
    ]
