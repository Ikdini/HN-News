# Generated by Django 4.1.2 on 2022-10-29 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_job_by_alter_job_text_alter_job_time_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('type', models.CharField(choices=[('job', 'Job'), ('story', 'Story'), ('comment', 'Comment'), ('poll', 'Poll'), ('pollopt', 'PollOpt')], max_length=10)),
                ('by', models.CharField(blank=True, max_length=100, null=True)),
                ('time', models.IntegerField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('descendants', models.IntegerField(blank=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-time'],
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='Story',
        ),
    ]