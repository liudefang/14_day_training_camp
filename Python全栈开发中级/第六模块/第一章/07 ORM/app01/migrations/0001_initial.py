# Generated by Django 2.1.1 on 2018-09-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=32)),
                ('publishData', models.DateField()),
                ('author', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('publish', models.CharField(max_length=32)),
            ],
        ),
    ]
