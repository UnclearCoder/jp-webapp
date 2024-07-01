from django.contrib import admin
from django.urls import path, re_path
from web_app import views

urlpatterns = [
    re_path(r"^$", views.home, name="home"),
    re_path(r"^centro-de-datos-macroeconomicos/$", views.macro, name="macro"),
    re_path(r"^ciclos-economicos/$", views.ciclos_economicos, name="ciclos_economicos"),
    re_path(r"^indicadores-mensuales/$", views.indicadores, name="indicadores"),
    re_path(r"^datos-demograficos/$", views.datos_demograficos, name="datos_demograficos"),
    re_path(r"^succesfull_page/$", views.succesfull_page, name="succesfull_page"),
    re_path(r"^JP-304-relacion-de-aportaciones-federales/$", views.JP_304, name="JP-304"),
    re_path(r"^IP-110-agricultura/$", views.IP_110, name="IP-110"),
    re_path(r"^JP-541-valor-de-la-inversion-en-obras-de-construccion/$", views.JP_541, name="JP-541"),
    re_path(r"^JP-361-transactions-in-pr-of-external-insurance-companies/$", views.JP_361, name="JP-361"),
    re_path(r"^JP-362-transacciones-con-el-exterior/$", views.JP_362, name="JP-362"),
    re_path(r"^JP-363-investment-in-securities-of-the-central-goverment/$", views.JP_363, name="JP-363"),
    re_path(r"^JP-560-63110-seguros-domesticos-de-vida/$", views.JP_560_63110, name="JP-560-63110"),
    re_path(r"^IP-210-mineria/$", views.IP_210, name="IP-210"),    
    re_path(r"^IP-220-utilidades/$", views.IP_220, name="IP-220"),
    re_path(r"^IP-230-construccion/$", views.IP_230, name="IP-230"),
    re_path(r"^IP-310-manufactura/$", views.IP_310, name="IP-310"),
    re_path(r"^JP-560-63111-organizaciones-de-servicio-de-salud/$", views.JP_560_63111, name="JP-560-63111"),
    re_path(r"^JP-560-63210-seguros-domesticos-propiedad-contingencia/$", views.JP_560_63210, name="JP-560-63210"),
    re_path(r"^JP-364-informacion-sobre-compañias de seguros/$", views.JP_364, name="JP-364"),
    re_path(r"^JP-375-encuesta-sobre-valor-pendinente/$", views.JP_375, name="JP-375"),
    re_path(r"^JP-362-transacciones-con-el-exterior-para-la-balanza/$", views.JP_362, name="JP-362"),
    re_path(r"^JP-560-2-preliminar/$", views.JP_560_2, name="JP-560-2"),
    re_path(r"^JP-383-pagos-de-asistencia/$", views.JP_383, name="JP-383"),
    re_path(r"^IP-480-transportacion/$", views.IP_480, name="IP-480"),
    re_path(r"^IP-420-comercio-al-por-mayor/$", views.IP_420, name="IP-420"),
    re_path(r"^IP-440-comercio-al-detal/$", views.IP_440, name="IP-440"),
    re_path(r"^IP-440g-estaciones-de-gasolina/$", views.IP_440g, name="IP-440g"),
    re_path(r"^Forms/$", views.Forms, name="Forms"),
]

