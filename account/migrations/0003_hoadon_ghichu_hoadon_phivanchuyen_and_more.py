# Generated by Django 5.0.4 on 2024-05-24 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_last_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='hoadon',
            name='GhiChu',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='hoadon',
            name='PhiVanChuyen',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hoadon',
            name='PhuongThucThanhToan',
            field=models.CharField(default='COD', max_length=100),
        ),
        migrations.AddField(
            model_name='hoadon',
            name='PhuongThucVanChuyen',
            field=models.CharField(default='Giao Nhanh', max_length=100),
        ),
        migrations.AddField(
            model_name='hoadon',
            name='TrangThai',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
