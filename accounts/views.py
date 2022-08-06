from re import template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView

from django.db.models import QuerySet
from django.views import View
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProfileForm
from .models import Profile, VaccinateInfo, DiaseseInfo
from .utils import secure_fio, secure_passport
import datetime


class ProfileView(LoginRequiredMixin, View):
    model = Profile
    form = ProfileForm
    template_name = "accounts/account.html"

    def get(self, request):
        return render(request, self.template_name, self.get_context_data())

    def post(self, request):
        context = self.get_context_data()
        bounded_form = self.form(request.POST, initial={'user': request.user})
        context['form'] = bounded_form
        if bounded_form.is_valid():
            obj = bounded_form.save()

        return render(request, self.template_name, context)

    def get_queryset(self) -> QuerySet:
        return self.model.objects.filter(user=self.request.user).first()

    def get_context_data(self) -> dict:
        instance = self.get_queryset()
        form = self.form(instance=instance)
        context = dict(
            form=form,
            object=instance,
        )
        return context


class Login(LoginView):
    next_page = '/'


class Logout(LogoutView):
    ...


class CertView(View):

    def get(self, request):
        context = self.get_context_data()
        return render(request=request,
                      template_name="accounts/includes/certificate.html",
                      context=context)

    def get_context_data(self):
        vac_data = VaccinateInfo.objects.filter(user=self.request.user)
        diasese = DiaseseInfo.objects.filter(user=self.request.user)
        profile = self.request.user.profile
        print(f"{vac_data=}")
        return dict(
            vac_data=vac_data,
            diasese=diasese,
            profile=profile
        )


# https://www.gosuslugi.ru/covid-cert/status/7f4c7f1d-0e39-4812-ba79-2cafa7da3f9c?lang=en
# gosuslug1ru

class CheckCertView(View):

    def get(self, request, cert_num):
        cert_num = " ".join(cert_num.split('_'))
        profile = Profile.objects.filter(cert_num=cert_num).first()
        passport_secure = secure_passport(profile.international_passport)
        full_name_secure = secure_fio(profile.full_name)
        vac = VaccinateInfo.objects.filter(user=request.user).last()
        context = dict(
            date_until=vac.vaccine_date + datetime.timedelta(days=183),
            passport_secure=passport_secure,
            full_name_secure=full_name_secure
        )
        return render(request, "accounts/check_cert.html", context)
