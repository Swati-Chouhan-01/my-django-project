# Generated by Django 4.1.6 on 2023-03-15 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_candidateinfo_github_profile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidateinfo',
            name='facebook_profile',
            field=models.CharField(blank='True', default='', max_length=50, null='True'),
        ),
    ]
