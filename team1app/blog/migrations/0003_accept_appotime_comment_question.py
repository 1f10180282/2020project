# Generated by Django 3.1 on 2020-11-25 16:17

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_schedule_scheduledata'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('finalup', models.DateTimeField(default=django.utils.timezone.now)),
                ('fromSt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.students')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tasks')),
                ('toTe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.teachers')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('isStudent', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tasks')),
            ],
        ),
        migrations.CreateModel(
            name='AppoTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now)),
                ('time', models.CharField(max_length=5)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tasks')),
            ],
        ),
        migrations.CreateModel(
            name='Accept',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(default=django.utils.timezone.now)),
                ('time', models.CharField(max_length=5)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.tasks')),
            ],
        ),
    ]
