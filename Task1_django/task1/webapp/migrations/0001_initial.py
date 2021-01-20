# Generated by Django 3.1.3 on 2021-01-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('father', models.CharField(max_length=50)),
                ('mother', models.CharField(max_length=50)),
                ('email', models.EmailField(default='abc@gmail.com', max_length=50)),
                ('degree', models.CharField(max_length=40)),
                ('gender', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]