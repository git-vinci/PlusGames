# Generated by Django 3.0.11 on 2020-12-27 03:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20201227_1216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=200, unique=True, verbose_name='メールアドレス'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(max_length=200, null=True, verbose_name='パスワード'),
        ),
    ]
