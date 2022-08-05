from email.policy import default
from hashlib import blake2b
from pyexpat import model
from re import U
from statistics import mode
from django.db import models
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import InMemoryUploadedFile
import qrcode
from django.conf import settings
from django.core.files import File

# Create your models here.

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, verbose_name="ФИО полностью", null=True, blank=True)
    bday = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
    passport_num = models.CharField(max_length=11, verbose_name="Серия номер документа идентификации", null=True, blank=True)
    international_passport = models.CharField(max_length=10, verbose_name="Международный паспорт")
    oms = models.CharField(max_length=20, verbose_name="ОМС", null=True, blank=True)
    snils = models.CharField(max_length=15, verbose_name="СНИЛС", null=True, blank=True)
    cert_num = models.CharField(max_length=20, verbose_name="Номер сертификата", default="", blank=True)
    SEX_CHOISE=(
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    sex = models.CharField(max_length=6, choices=SEX_CHOISE, verbose_name="Пол")
    qr_code = models.ImageField(upload_to="qrcode/", null=True, blank=True, default=None)
    
    def __str__(self) -> str:
        return f"{self.full_name}"

    @property
    def qr_code_url(self):
        return self.qr_code

    def save(self, **kwargs) -> None:
        if self.qr_code:
            return super().save(**kwargs)
        qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
                )
        qr.add_data(f"http://{settings.DOMAIN_NAME}/covid-cert/status/{'_'.join(self.cert_num.split('_'))}")
        img = qr.make_image(fill_color="black", back_color="white")
        path = f"temp/{self.user}_{self.cert_num}.png"
        img.save(path)
        with open(path, 'rb') as f:
            my_file = File(f)
            filename = f"{self.user}_{self.cert_num}.png"
            self.qr_code.save(filename, my_file)
        return super().save(**kwargs)


class VaccinateInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vaccine_date = models.DateField(verbose_name="Дата вакцинации", null=True, blank=True)
    record_number = models.CharField(max_length=20, verbose_name="Номер записи о вакцинации", null=True, blank=True)
    series = models.CharField(max_length=6, verbose_name="Номер вакцины") # 050621


class DiaseseInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record_number = models.CharField(max_length=20, verbose_name="Номер записи о болезни")
    recovery_date = models.DateField(verbose_name="Дата выздоровления")




