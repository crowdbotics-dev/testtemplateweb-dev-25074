# Generated by Django 2.2.26 on 2022-06-24 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HGHG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cv', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]
