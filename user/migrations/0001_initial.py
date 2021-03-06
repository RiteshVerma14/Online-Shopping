# Generated by Django 3.1 on 2020-09-18 13:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=70)),
                ('mob_no', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('msg', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField()),
                ('user_id', models.CharField(max_length=50)),
                ('remark', models.TextField(max_length=1000)),
                ('status', models.BooleanField()),
                ('order_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='sign_up',
            fields=[
                ('u_name', models.CharField(max_length=50)),
                ('u_email', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('u_mob_no', models.CharField(max_length=25, unique=True)),
                ('u_img', models.ImageField(null=True, upload_to='static/images/')),
                ('u_password', models.CharField(max_length=50)),
                ('u_address', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='subcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('dis_price', models.FloatField()),
                ('size', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=30)),
                ('descriptions', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('img', models.ImageField(default='', upload_to='static/images/')),
                ('subcategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.subcategory')),
            ],
        ),
    ]
