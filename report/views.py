from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string

from .forms import LeadForm, CheckoutForm, ContactForm, BecomePublisherFrom
from .models import Category, Report, Publisher, SliderImage, OurClients, Billing_Details
from django.db.models import Q
from django_countries import countries
from django.core.mail import send_mail
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import JsonResponse
import json
import requests


def indexView(request):
    reports = Report.objects.all().order_by('-published_date')[:3]
    categories1 = Category.objects.all().order_by("name")[:10]
    categories2 = Category.objects.all().order_by("name")[10:]
    publishers = Publisher.objects.all().order_by("name")
    query = request.GET.get('searchReport')
    slider = SliderImage.objects.all()
    clients = OurClients.objects.all()

    return render(request, 'base/index.html',
                  {'reports': reports, 'categories1': categories1, 'categories2': categories2, 'slider': slider,
                   'publishers': publishers, 'clients': clients})


def aboutus(request):
    return render(request, 'base/about-us.html')


def servicesPage(request):
    return render(request, 'base/services.html')


def research_methodology(request):
    return render(request, 'base/research_methodology.html')


def refund_policy(request):
    return render(request, 'base/refund-policy.html')


def contactus(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            emailBody = 'Full Name:' + request.POST['full_name'] + '\n\n' + 'Corporate Email:' + request.POST[
                'corporate_email'] + '\n\n' + 'Phone:' + request.POST['phone'] \
                        + '\n\n' + 'Subject: ' + request.POST['subject'] + '\n\n' + 'Message:' + request.POST['message']
            send_mail(
                'Contact Us Request',
                emailBody,
                'sales@wisdommarketresearch.com',
                ['leads@affluencemarketreports.com'],
                fail_silently=False,
            )

            return redirect('thankyou')
    return render(request, 'base/contact-us.html', {'form': form})


def reportPage(request, slug):
    report = get_object_or_404(Report, slug=slug)
    category = report.category
    cat_report = Report.objects.filter(category=category)[:5]
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead_form = form.save(commit=False)
            lead_form.report = report
            lead_form.request_type = 'Request Sample'
            if request.POST['comment'] == "":
                lead_form.comment = ""
            lead_form.save()
            message = 'Report Code:' + report.publisher.publisher_code + '-' + str(
                report.id) + '\n\n' + 'Report Name:' + report.title + '\n\n' + 'Client Name:' + lead_form.full_name + '\n\n' 'Client Email: ' + lead_form.corporate_email + '\n\n' + 'Phone:' + str(
                lead_form.phone) + '\n\n' + 'Country:' + str(
                lead_form.country) + '\n\n' + 'Category:' + report.category.name + '\n\n' + 'Publisher :' + report.publisher.name + '\n\n' + 'Company:' + lead_form.company + '\n\n' + 'Job Title:' + lead_form.job_title + '\n\n' + 'Price:' + str(
                report.single_user_price) + '\n\n' + 'Comments:' + lead_form.comment
            subject = 'Lead - Sample Request'
            # send_mail(
            #     'Lead - Sample Request',
            #     emailBody,
            #     'sales@wisdommarketresearch.com',
            #     ['leads@affluencemarketreports.com'],
            #     fail_silently=False,
            # )
            # send_simple_message(lead_form.full_name, report.title, lead_form.corporate_email)
            send_email(sender_email, sender_password, recipient_email, subject, message)

            return redirect('thankyou')
        else:
            print('Form invalid')
    else:
        form = LeadForm()

    return render(request, 'report/reportpage.html',
                  {'report': report, 'category': category, 'cat_report': cat_report, 'form': form})


def thankyouPage(request):
    return render(request, 'base/thank-you.html')


def publisher_list(request):
    publishers = Publisher.objects.all().order_by("name")
    return render(request, 'report/publisher_list.html', {'publishers': publishers})


def requestSample(request, id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        form = LeadForm(request.POST)

        if form.is_valid():
            lead_form = form.save(commit=False)
            lead_form.report = report
            lead_form.request_type = 'Request Sample'
            if request.POST['comment'] == "":
                lead_form.comment = ""

            lead_form.save()

            message = 'Report Code:' + report.publisher.publisher_code + '-' + str(
                report.id) + '\n\n' + 'Report Name:' + report.title + '\n\n' + 'Client Name:' + lead_form.full_name + '\n\n' 'Client Email: ' + lead_form.corporate_email + '\n\n' + 'Phone:' + str(
                lead_form.phone) + '\n\n' + 'Country:' + str(
                lead_form.country) + '\n\n' + 'Category:' + report.category.name + '\n\n' + 'Publisher :' + report.publisher.name + '\n\n' + 'Company:' + lead_form.company + '\n\n' + 'Job Title:' + lead_form.job_title + '\n\n' + 'Price:' + str(
                report.single_user_price) + '\n\n' + 'Comments:' + lead_form.comment
            subject = 'Lead - Sample Request'
            # send_mail(
            #     'Lead - Sample Request',
            #      emailBody,
            #     'sales@wisdommarketresearch.com',
            #     ['leads@affluencemarketreports.com'],
            #     fail_silently=False,
            # )
            # send_simple_message(lead_form.full_name, report.title, lead_form.corporate_email)
            # send_email(sender_email, receiver_email, subject, message, smtp_server, smtp_port, username, password)

            send_email(sender_email, sender_password, recipient_email, subject, message)
            return redirect('thankyou')
        else:
            print('Form invalid')
    else:
        form = LeadForm()
    return render(request, 'report/request-sample.html', {'form': form, 'report': report})


def requestDiscount(request, id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead_form = form.save(commit=False)
            lead_form.report = report
            lead_form.request_type = 'Request Discount'
            if request.POST['comment'] == "":
                lead_form.comment = ""
            lead_form.save()
            message = 'Report Code:' + report.publisher.publisher_code + '-' + str(
                report.id) + '\n\n' + 'Report Name:' + report.title + '\n\n' + 'Client Name:' + lead_form.full_name + '\n\n' 'Client Email: ' + lead_form.corporate_email + '\n\n' + 'Phone:' + str(
                lead_form.phone) + '\n\n' + 'Country:' + str(
                lead_form.country) + '\n\n' + 'Category:' + report.category.name + '\n\n' + 'Publisher :' + report.publisher.name + '\n\n' + 'Company:' + lead_form.company + '\n\n' + 'Job Title:' + lead_form.job_title + '\n\n' + 'Price:' + str(
                report.single_user_price) + '\n\n' + 'Comments:' + lead_form.comment
            subject = 'Lead - Discount Request'
            # send_mail(
            #     'Lead - Discount Request',
            #      emailBody,
            #     'sales@wisdommarketresearch.com',
            #     ['leads@affluencemarketreports.com'],
            #     fail_silently=False,
            # )
            # send_simple_message(lead_form.full_name, report.title, lead_form.corporate_email)
            send_email(sender_email, sender_password, recipient_email, subject, message)
            return redirect('thankyou')
        else:
            print('Form invalid')
    else:
        form = LeadForm()
    return render(request, 'report/request-discount.html', {'form': form, 'report': report})


def requestInquiry(request, id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead_form = form.save(commit=False)
            lead_form.report = report
            lead_form.request_type = 'Request Inquiry'
            if request.POST['comment'] == "":
                lead_form.comment = ""
            lead_form.save()
            message = 'Report Code:' + report.publisher.publisher_code + '-' + str(
                report.id) + '\n\n' + 'Report Name:' + report.title + '\n\n' + 'Client Name:' + lead_form.full_name + '\n\n' 'Client Email: ' + lead_form.corporate_email + '\n\n' + 'Phone:' + str(
                lead_form.phone) + '\n\n' + 'Country:' + str(
                lead_form.country) + '\n\n' + 'Category:' + report.category.name + '\n\n' + 'Publisher :' + report.publisher.name + '\n\n' + 'Company:' + lead_form.company + '\n\n' + 'Job Title:' + lead_form.job_title + '\n\n' + 'Price:' + str(
                report.single_user_price) + '\n\n' + 'Comments:' + lead_form.comment
            subject = 'Lead - Inquiry Before Buying Request'
            # send_mail(
            #     'Lead - Inquiry Before Buying Request',
            #      emailBody,
            #     'sales@wisdommarketresearch.com',
            #     ['leads@affluencemarketreports.com'],
            #     fail_silently=False,
            # )
            # send_simple_message(lead_form.full_name, report.title, lead_form.corporate_email)
            send_email(sender_email, sender_password, recipient_email, subject, message)
            return redirect('thankyou')
        else:
            print('Form invalid')
    else:
        form = LeadForm()
    return render(request, 'report/request-inquiry.html', {'form': form, 'report': report})


def indexcheckout(request, id, price):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        form = CheckoutForm()
        price = price
        order_amount = price * 100
        order_currency = 'USD'
        client = razorpay.Client(auth=('rzp_live_p0Q8CMyKAt08f9', 'xPSeOhGJTV1VlyEbbXzuFAcX'))
        payment = client.order.create({'amount': order_amount, 'currency': order_currency, 'payment_capture': '1'})
        print(payment)
        print("Payment Successfull")
        return render(request, 'report/checkout.html',
                      {'report': report, 'price': price, 'payment': payment, 'form': form})
    form = CheckoutForm()
    return render(request, 'report/checkout.html', {'report': report, 'form': form, 'price': price})


def checkout(request, id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        price = int(request.POST['price'])
        form = CheckoutForm()
        order_amount = price * 100
        order_currency = 'USD'
        client = razorpay.Client(auth=('rzp_live_p0Q8CMyKAt08f9', 'xPSeOhGJTV1VlyEbbXzuFAcX'))
        payment = client.order.create({'amount': order_amount, 'currency': order_currency, 'payment_capture': '1'})

        return render(request, 'report/checkout.html',
                      {'report': report, 'form': form, 'price': price, 'payment': payment})


def categoryPage(request, slug):
    category = get_object_or_404(Category, slug=slug)
    reports = Report.objects.filter(category=category).order_by('-published_date')
    all_categories = Category.objects.all().order_by("name")

    paginator = Paginator(reports, 10)
    page_number = request.GET.get('page')
    try:
        reports = paginator.page(page_number)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render(request, 'report/category.html',
                  {'category': category, 'reports': reports, 'all_categories': all_categories})


def publisherPage(request, slug):
    publisher = get_object_or_404(Publisher, slug=slug)
    reports = Report.objects.filter(publisher=publisher).order_by('-published_date')
    all_publishers = Publisher.objects.all().order_by("name")
    paginator = Paginator(reports, 10)
    page_number = request.GET.get('page')
    try:
        reports = paginator.page(page_number)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render(request, 'report/publisher.html',
                  {'publisher': publisher, 'reports': reports, 'all_publishers': all_publishers})


def latestReports(request):
    reports = Report.objects.all().order_by('-published_date')
    all_categories = Category.objects.all().order_by("name")
    paginator = Paginator(reports, 10)
    page_number = request.GET.get('page')
    try:
        reports = paginator.page(page_number)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render(request, 'report/latest-report.html', {'reports': reports, 'all_categories': all_categories})


# def searchReports(request):
#     ctx = {}
#     url_parameter = request.GET.get("q")
#     if url_parameter:
#         searchreports = Report.objects.filter(title__icontains=url_parameter)
#     else:
#         searchreports = Report.objects.all()
#
#     ctx["searchreports"] = searchreports
#
#     if request.is_ajax():
#         html = render_to_string(
#             template_name="base/partial-result.html",
#             context={"searchreports": searchreports}
#         )
#         data_dict = {"html_from_view": html}
#         return JsonResponse(data=data_dict, safe=False)
#
#     return render(request, 'base/index.html',ctx)


def search_report_list(request):
    query = request.GET.get("searchquery")
    if query:
        reports = Report.objects.filter(title__icontains=query)
    else:
        # return render(request, '404.html', status=404)
        return redirect('latestreports')

    paginator = Paginator(reports, 10)
    page_number = request.GET.get('page')
    try:
        reports = paginator.page(page_number)
    except PageNotAnInteger:
        reports = paginator.page(1)
    except EmptyPage:
        reports = paginator.page(paginator.num_pages)
    return render(request, 'report/search_report.html', {'reports': reports, 'query': query})


def paymentComplete(request):
    body = json.loads(request.body)
    print('BODY:', body)
    product = Report.objects.get(id=body['reportId'])
    # Order.objects.create(
    # 	product=product
    # 	)

    return JsonResponse('Payment completed!', safe=False)


def privacyPolicy(request):
    return render(request, 'base/privacy-policy.html')


def termsandconditions(request):
    return render(request, 'base/terms-and-conditions.html')


def index_header(request):
    return render(request, 'base/index-header.html')


def handler404(request):
    return render(request, '404.html', status=404)


def become_publisher(request):
    if request.method == "GET":
        form = BecomePublisherFrom()
    else:
        form = BecomePublisherFrom(request.POST)
        if form.is_valid():
            form.save()
            emailBody = 'First Name:' + request.POST['first_name'] + '\n\n' + 'Last Name:' + request.POST[
                'last_name'] + '\n\n' + 'Publisher Email:' + request.POST['corporate_email'] + '\n\n' + 'Phone:' + str(
                request.POST['phone']) + '\n\n' + 'Company:' + request.POST['company'] + '\n\n' + 'Company Website:' + \
                        request.POST['website'] + '\n\n' + 'Company Description :' + request.POST[
                            'intro'] + '\n\n' + 'No. Of Report:' + request.POST[
                            'no_of_report'] + '\n\n' + 'Yearly Published Reports:' + request.POST['yearly_published']
            # emailBody="Test mail"
            send_mail(
                'Publisher Partnership - Praposal',
                emailBody,
                'sales@wisdommarketresearch.com',
                ['sales@wisdommarketresearch.com'],
                fail_silently=False,
            )
            print("email send successfully")
            return redirect('thankyou')

    return render(request, 'base/become-publisher.html', {'form': form})


def covid_request(request, id):
    report = get_object_or_404(Report, id=id)
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            lead_form = form.save(commit=False)
            lead_form.report = report
            lead_form.request_type = 'COVID-19 Request'
            if request.POST['comment'] == "":
                lead_form.comment = ""
            lead_form.save()
            emailBody = 'Report Code:' + report.publisher.publisher_code + '-' + str(
                report.id) + '\n\n' + 'Report Name:' + report.title + '\n\n' + 'Client Name:' + lead_form.full_name + '\n\n' 'Client Email: ' + lead_form.corporate_email + '\n\n' + 'Phone:' + str(
                lead_form.phone) + '\n\n' + 'Country:' + str(
                lead_form.country) + '\n\n' + 'Category:' + report.category.name + '\n\n' + 'Publisher :' + report.publisher.name + '\n\n' + 'Company:' + lead_form.company + '\n\n' + 'Job Title:' + lead_form.job_title + '\n\n' + 'Price:' + str(
                report.single_user_price) + '\n\n' + 'Comments:' + lead_form.comment
            send_mail(
                'Lead - COVID-19 Impact Request',
                emailBody,
                'sales@wisdommarketresearch.com',
                ['leads@affluencemarketreports.com'],
                fail_silently=False,
            )
            send_simple_message(lead_form.full_name, report.title, lead_form.corporate_email)
            return redirect('thankyou')
        else:
            print('Form invalid')
    else:
        form = LeadForm()
    return render(request, 'report/covid19-request.html', {'form': form, 'report': report})


def subscribeForm(request):
    if request.method == "POST":
        email = request.POST["email"]
        emailbody = 'You received subscription request from ' + email
        send_mail(
            'Subscription Request',
            emailbody,
            'sales@wisdommarketresearch.com',
            ['leads@affluencemarketreports.com'],
            fail_silently=False,
        )
        send_simple_message()

    return redirect('thankyou')


import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl


def send_email(sender_email, sender_password, recipient_email, subject, message):
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Attach the message to the email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Create a secure SSL/TLS connection with the SMTP server
        server = smtplib.SMTP_SSL('smtp.zoho.in', 465)  # Replace with your SMTP server address and port

        # Log in to the email account
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, recipient_email, msg.as_string())

        # Close the connection
        server.quit()

        print('Email sent successfully!')
    except Exception as e:
        print('An error occurred while sending the email:', str(e))


sender_email = "wmr@wisdommarketresearch.net"
recipient_email = "leads@wisdommarketresearch.com"
sender_password = "Nopassword@890"


def send_simple_message(name, title, email):
    return requests.post(
        "https://api.mailgun.net/v3/www.affluencemarketreports.com/messages",
        auth=("api", "33f0f7064e487ae726945341954eb2b8-aff2d1b9-e40e397e"),
        data={"from": "abhi.j@affluencemarketreports.com",
              "to": [email],
              "subject": "Sample Request for Report " + title,
              "text": "Dear " + name + ",\n\nGreetings from Wisdom Market Research!!\n\n"
                                       "Thank you for showing interest in the report- Report Title -" + title + "\n\nWe will reach out to you within 24 hours for further assistance.\n\n"
                                                                                                                "You can reply to this email if you have more details to add,or you can also call our team at +1-424-256-1722 and we will make sure to address it."
                                                                                                                "\n\nThanks and Best Regards,\n\nWisdom Market Research."
                                                                                                                "\n\nTel: +91 8591633987 \n\n E-mail: sales@wisdommarketresearch.com\n\nWebsite: www.wisdommarketresearch.com"})


import razorpay
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime


@csrf_exempt
def success(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    address = request.POST.get('address[]')
    phone = request.POST['phone']
    company = request.POST['company']
    country = request.POST['country']
    city = request.POST['city']
    state = request.POST['state']
    zipcode = request.POST['zipcode']
    job_title = request.POST['job_title']
    corporate_email = request.POST['corporate_email']
    report_id = request.POST['report']
    price = request.POST['price']
    report = Report.objects.get(id=report_id)
    invoice_date = datetime.now()
    obj = Billing_Details.objects.create(first_name=first_name, last_name=last_name, address=address,
                                         phone=phone, company=company, city=city, job_title=job_title,
                                         zipcode=zipcode, corporate_email=corporate_email, state=state,
                                         report=report, invoice_date=invoice_date, amount=price)
    obj.save()
    emailBody = 'Report Code:' + report.publisher.publisher_code + '-' + str(
        report.id) + '\n\n' + 'Report Name:' + report.title + '\n\n' + 'Client Name:' + first_name + '\n\n' 'Client Email: ' + corporate_email + '\n\n' + 'Phone:' + str(
        phone) + '\n\n' + 'Country:' + country + '\n\n' + 'Category:' + report.category.name + '\n\n' + 'Publisher :' + report.publisher.name + '\n\n' + 'Company:' + company + '\n\n' + 'Job Title:' + job_title + '\n\n' + 'Price:' + price + '\n\n'
    send_mail(
        'Razorpay Payment Received',
        emailBody,
        'sales@wisdommarketresearch.com',
        ['leads@wisdommarketresearch.com'],
        fail_silently=False,
    )
    return redirect('thankyou')
