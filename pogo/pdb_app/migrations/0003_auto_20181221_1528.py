# Generated by Django 2.1.4 on 2018-12-21 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pdb_app', '0002_catagory'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
    ]