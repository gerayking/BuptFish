# Generated by Django 3.1.2 on 2020-12-07 00:52

import apps.user.models
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='favorites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_id', models.IntegerField(default=0)),
                ('user', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'favorites',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('goods_id', models.AutoField(primary_key=True, serialize=False)),
                ('goods_name', models.CharField(max_length=50)),
                ('picture', models.CharField(max_length=100)),
                ('class_id', models.IntegerField(default=0)),
                ('price', models.FloatField()),
                ('secprice', models.FloatField()),
                ('condition', models.CharField(max_length=50)),
                ('user_name', models.CharField(max_length=20)),
                ('goods_num', models.IntegerField()),
            ],
            options={
                'db_table': 'Goods',
            },
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('mes_id', models.IntegerField(primary_key=True, serialize=False)),
                ('mes_type', models.IntegerField(default=1)),
                ('user_name', models.CharField(max_length=50)),
                ('mes_content', models.CharField(max_length=200)),
                ('res_id', models.IntegerField(null=True)),
                ('goods_id', models.IntegerField(default=0)),
                ('mes_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'Messages',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField()),
                ('buyer_id', models.IntegerField()),
                ('seller_id', models.IntegerField()),
                ('rec_name', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('tel', models.IntegerField()),
                ('email', models.CharField(max_length=20)),
                ('order_time', models.DateTimeField()),
                ('cost', models.FloatField()),
                ('state', models.CharField(max_length=20)),
                ('send', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Order',
            },
        ),
        migrations.CreateModel(
            name='Orderdetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_id', models.IntegerField()),
                ('order_id', models.IntegerField(default=0)),
                ('goods_id', models.IntegerField(default=0)),
                ('goods_name', models.CharField(max_length=20)),
                ('goods_price', models.FloatField()),
                ('goods_num', models.IntegerField()),
                ('goods_cost', models.FloatField()),
            ],
            options={
                'db_table': 'Orderdetail',
            },
        ),
        migrations.CreateModel(
            name='Type_id',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.IntegerField(default=0)),
                ('class_name', models.CharField(max_length=50)),
                ('father_id', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'Type_id',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(default='https://i.loli.net/2020/11/08/KnofmQWD15BxcMu.jpg', upload_to=apps.user.models.user_director_path, verbose_name='头像')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
