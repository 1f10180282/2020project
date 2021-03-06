# Generated by Django 3.1 on 2020-11-24 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.IntegerField(default=0)),
                ('start', models.CharField(max_length=5)),
                ('end', models.CharField(max_length=5)),
                ('schedule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.schedule')),
            ],
        ),
    ]
