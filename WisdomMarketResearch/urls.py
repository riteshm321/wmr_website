"""WisdomMarketResearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
# from report.sitemaps import ReportSitemap
from report.views import (indexView,categoryPage,publisherPage,aboutus,contactus,
                          latestReports,thankyouPage,search_report_list,servicesPage,subscribeForm,
                          privacyPolicy,termsandconditions,index_header,become_publisher,publisher_list,success,research_methodology,refund_policy)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexView, name='index'),
    path('index/', index_header, name='indexheader'),
    path('latest-reports/', latestReports, name='latestreports'),
    path('about-us/', aboutus, name='aboutus'),
    path('research-methodology/', research_methodology, name='research_methodology'),
    path('refund-policy/', refund_policy, name='refund_policy'),
    path('contact-us/', contactus, name='contactus'),
    path('thank-you/', thankyouPage, name='thankyou'),
    path('search-reports/', search_report_list, name='search_report_list'),
    path('services/', servicesPage, name='services'),
    path('privacy-policy/', privacyPolicy, name='privacypolicy'),
    path('terms-and-conditions/', termsandconditions, name='termsandconditions'),
    path('category/<slug:slug>/', categoryPage, name='category'),
    path('publisher/<slug:slug>/', publisherPage, name='publisher'),
    path('publisher/', publisher_list, name='publisher_list'),
    path('become-publisher/', become_publisher, name='becomepublisher'),
    path('subscribe/', subscribeForm, name='subscribe'),
    path('success/', success, name='success'),
    path('industry-analysis/', include('report.urls', namespace='reports')),
    path("robots.txt",TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
    path('sitemap.xml', TemplateView.as_view(template_name="sitemap.xml", content_type="text/plain"),),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + \
              static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
