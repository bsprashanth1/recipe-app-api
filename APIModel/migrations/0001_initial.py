# Generated by Django 2.1.5 on 2019-02-07 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UIModel',
            fields=[
                ('request_id', models.IntegerField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('inputText', models.TextField(blank=True, default='', max_length=2000)),
                ('inputType', models.CharField(blank=True, default='text', max_length=10)),
                ('keywords', models.TextField(blank=True, max_length=200)),
                ('totalScenarios', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'ordering': ('request_id',),
            },
        ),
    ]
