# Generated by Django 3.1.2 on 2020-12-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qwerty', '0005_auto_20201228_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
