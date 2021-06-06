# Generated by Django 3.2.4 on 2021-06-06 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30, null=True)),
                ('access_level', models.CharField(choices=[('Tr', 'Traverse Folder'), ('RW', 'Read and Write'), ('FA', 'Full Access')], max_length=50)),
            ],
        ),
    ]