from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap
from .views import health

sitemaps = {
    "static": StaticViewSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('privacy-policy/', views.privacy, name='privacy'),
    path('terms-of-use/', views.terms, name='terms'),
    path(
        "sitemap.xml",sitemap,
        {"sitemaps": sitemaps},
        name="django.contrib.sitemaps.views.sitemap",
    ),
    path("health/", health),
]