# Generated by Django 4.1 on 2022-08-05 23:00

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
            name='VaccinateInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vaccine_date', models.DateField(blank=True, null=True, verbose_name='Дата вакцинации')),
                ('record_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='Номер записи о вакцинации')),
                ('series', models.CharField(max_length=6, verbose_name='Номер вакцины')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='ФИО полностью')),
                ('bday', models.DateField(blank=True, null=True, verbose_name='Дата рождения')),
                ('passport_num', models.CharField(blank=True, max_length=11, null=True, verbose_name='Серия номер документа идентификации')),
                ('international_passport', models.CharField(max_length=10, verbose_name='Международный паспорт')),
                ('oms', models.CharField(blank=True, max_length=20, null=True, verbose_name='ОМС')),
                ('snils', models.CharField(blank=True, max_length=15, null=True, verbose_name='СНИЛС')),
                ('cert_num', models.CharField(blank=True, default='', max_length=20, verbose_name='Номер сертификата')),
                ('sex', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, verbose_name='Пол')),
                ('qr_code', models.ImageField(blank=True, default=None, null=True, upload_to='qrcode/')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DiaseseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('record_number', models.CharField(max_length=20, verbose_name='Номер записи о болезни')),
                ('recovery_date', models.DateField(verbose_name='Дата выздоровления')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
