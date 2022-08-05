from django.urls import path
from .views import ProfileView, Login, Logout, CertView, CheckCertView


urlpatterns = [
    path('', ProfileView.as_view(), name='profile'),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("cert/", CertView.as_view(), name='cert'),
    path("covid-cert/status/<str:cert_num>", CheckCertView.as_view(), name="cert_check")
]
