# Generated by Django 2.2.6 on 2019-11-26 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telegram', '0015_auto_20191126_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseReason',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'обработчик',
                'verbose_name_plural': 'обработчики',
            },
        ),
        migrations.DeleteModel(
            name='Reason',
        ),
        migrations.CreateModel(
            name='TriggerReason',
            fields=[
                ('basereason_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='telegram.BaseReason')),
                ('type', models.CharField(choices=[('Reason', 'apps.common.secret_note.reasons'), ('Reason', 'apps.common.other_app.reasons'), ('Reason', 'apps.common.second_one_app.reasons')], default=None, max_length=500, null=True, verbose_name='Обработчик')),
            ],
            options={
                'verbose_name': 'обработчик',
                'verbose_name_plural': 'обработчики',
            },
            bases=('telegram.basereason',),
        ),
    ]