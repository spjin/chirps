# Generated by Django 2.0.2 on 2018-04-02 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('announcements', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='approver',
        ),
        migrations.RemoveField(
            model_name='announcement',
            name='submitter',
        ),
    ]