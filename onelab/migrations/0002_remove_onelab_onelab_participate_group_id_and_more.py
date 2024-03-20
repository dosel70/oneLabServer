# Generated by Django 5.0.2 on 2024-03-19 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onelab', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='onelab',
            name='onelab_participate_group_id',
        ),
        migrations.RemoveField(
            model_name='onelab',
            name='onelab_participate_url',
        ),
        migrations.RemoveField(
            model_name='onelab',
            name='onelab_title',
        ),
        migrations.AddField(
            model_name='onelab',
            name='onelab_ask_email',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onelab',
            name='onelab_detail_content',
            field=models.CharField(default=1, max_length=2000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onelab',
            name='onelab_main_title',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='onelab',
            name='onelab_max_count',
            field=models.SmallIntegerField(default=2, max_length=10),
        ),
        migrations.AddField(
            model_name='onelab',
            name='onelab_url',
            field=models.CharField(default='http://localhost:', max_length=300),
        ),
        migrations.AlterField(
            model_name='onelab',
            name='onelab_content',
            field=models.CharField(max_length=100),
        ),
    ]
