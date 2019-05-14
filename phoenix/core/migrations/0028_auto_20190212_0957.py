# Generated by Django 2.1.3 on 2019-02-12 09:57

from django.db import migrations


def migrate_systems_affected(apps, schema_editor):
    System = apps.get_model('core', 'System')
    OutageHistory = apps.get_model('core', 'OutageHistory')
    for system in System.objects.all():
        for outage in system.outage_set.all():
            outage.systems_affected = system
            outage.save()
            for outage_history in OutageHistory.objects.filter(outage_id=outage.id):
                outage_history.systems_affected = system
                outage_history.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_auto_20190212_0810'),
    ]

    operations = [
         migrations.RunPython(migrate_systems_affected),
        migrations.RemoveField(
            model_name='outage',
            name='systems_affected_bck',
        ),
        migrations.RemoveField(
            model_name='outagehistory',
            name='systems_affected_bck',
        ),
    ]
