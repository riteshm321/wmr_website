




from django.urls import path
from report.views import (reportPage,requestSample,checkout,requestInquiry,
                          requestDiscount,paymentComplete,covid_request,indexcheckout)
app_name = 'reports'

urlpatterns = [

    path('<slug:slug>/', reportPage, name='reportpage'),
    path('request-sample/<int:id>/', requestSample, name='samplerequest'),
    path('request-discount/<int:id>/', requestDiscount, name='discountrequest'),
    path('request-inquiry/<int:id>/', requestInquiry, name='inquiryrequest'),
    path('covid19-request/<int:id>/', covid_request, name='covidrequest'),
    path('checkout/<int:id>/', checkout, name='checkout'),
    path('checkout/<int:id>/<int:price>', indexcheckout, name='indexcheckout'),
    path('payment/complete/', paymentComplete, name='complete'),


]


