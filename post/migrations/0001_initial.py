# Generated by Django 3.0.7 on 2020-10-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, max_length=400, null=True)),
                ('creat_at', models.DateTimeField(auto_now_add=True)),
                ('comment_count', models.IntegerField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
