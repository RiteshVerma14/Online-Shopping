# Generated by Django 3.1 on 2020-09-19 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200919_1443'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sign_up',
            old_name='Address',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='sign_up',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='sign_up',
            old_name='Img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='sign_up',
            old_name='Mob_no',
            new_name='mob_no',
        ),
        migrations.RenameField(
            model_name='sign_up',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='sign_up',
            old_name='Password',
            new_name='password',
        ),
    ]
