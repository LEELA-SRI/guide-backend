# Generated by Django 4.0.4 on 2023-02-18 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0044_alter_guide_myimage_alter_team_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='document',
            field=models.FileField(blank=True, null=True, upload_to='documents/<django.db.models.fields.CharField>'),
        ),
    ]
