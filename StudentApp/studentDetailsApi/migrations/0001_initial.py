# Generated by Django 4.0.1 on 2022-01-23 14:51

from django.db import migrations, models
import studentDetailsApi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentTShirtDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('age', models.IntegerField(validators=[studentDetailsApi.models.validate_age])),
                ('email_id', models.EmailField(max_length=254)),
                ('section', models.CharField(choices=[('P', 'Primary'), ('U', 'Upper-Primary')], max_length=1)),
                ('shirt_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1)),
                ('guardian_name', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
