# Generated by Django 4.2.7 on 2023-11-23 01:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Saving_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('dcls_month', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('join_member', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('like_users', models.ManyToManyField(null=True, related_name='like_saving', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Saving_Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField(default=-1, null=True)),
                ('intr_rate2', models.FloatField(default=-1, null=True)),
                ('save_trm', models.IntegerField()),
                ('rsrv_type', models.TextField()),
                ('saving_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saving_options', to='compare_deposit.saving_products')),
            ],
        ),
        migrations.CreateModel(
            name='Deposit_Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField(unique=True)),
                ('dcls_month', models.TextField()),
                ('kor_co_nm', models.TextField()),
                ('fin_prdt_nm', models.TextField()),
                ('join_way', models.TextField()),
                ('join_member', models.TextField()),
                ('spcl_cnd', models.TextField()),
                ('etc_note', models.TextField()),
                ('join_deny', models.IntegerField()),
                ('like_users', models.ManyToManyField(null=True, related_name='like_deposit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Deposit_Options',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fin_prdt_cd', models.TextField()),
                ('intr_rate_type_nm', models.CharField(max_length=100)),
                ('intr_rate', models.FloatField(default=-1, null=True)),
                ('intr_rate2', models.FloatField(default=-1, null=True)),
                ('save_trm', models.IntegerField()),
                ('deposit_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deposit_options', to='compare_deposit.deposit_products')),
            ],
        ),
    ]
