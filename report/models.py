
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from ckeditor.fields import RichTextField
from django.urls import *
from django.dispatch import receiver
from django.contrib.auth.models import User


class Report(models.Model):
    title = models.CharField(max_length=1000)
    keyword = models.CharField(max_length=1000)
    meta_title = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True, blank=True,null=True,max_length=255)
    url = models.URLField(unique=True, blank=True,null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    publisher = models.ForeignKey('Publisher', models.CASCADE)
    summary = RichTextField()
    tabel_of_content = RichTextField()
    list_of_figures = RichTextField(blank=True,null=True)
    published_date = models.DateField()
    no_of_pages = models.IntegerField(default=100)
    strategic_report = models.IntegerField(default=899)
    quantitative_report = models.IntegerField(default=1650)
    single_user_price = models.IntegerField(default=3650)
    multi_user_price = models.IntegerField(default=4500)
    corporate_user_price = models.IntegerField(default=6500)

    # upload_by = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('reports:reportpage',args=[self.slug])


@receiver(post_save, sender=Report)
def post_save_slug_generator(sender,instance, created, *args, **kwargs):
    if created:
        if not instance.slug:
            url = str(instance.keyword) + '-' + str(instance.id)
            instance.slug = slugify(url)
            instance.url = 'http://www.wisdommarketresearch.com/' + slugify(url)
            instance.save()

# post_save.connect(post_save_slug_generator,sender=Report)


class SliderImage(models.Model):
    header = models.CharField(max_length=200,blank=True, null=True)
    tagline = models.CharField(max_length=200,blank=True, null=True)
    image = models.ImageField(upload_to='slider/', blank=True, null=True)

    def __str__(self):
        return str(self.image.name)




class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,unique=True)
    image = models.ImageField(upload_to='category/', blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    publisher_code = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,unique=True)
    image = models.ImageField(upload_to='publishers/', blank=True, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(Publisher,self).save(*args,**kwargs)


from django_countries.fields import CountryField
# Create your models here.


class Lead(models.Model):
    LEAD_TYPE =(
        ('Request Sample','Request Sample'),
        ('Request Discount', 'Request Discount'),
        ('Request Inquiry', 'Request Inquiry'),
        ('COVID-19 Request','COVID-19 Request')

    )
    report = models.ForeignKey(Report,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    corporate_email = models.EmailField()
    country = CountryField(blank_label='Select Country')
    phone = models.CharField(max_length=14)
    job_title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    comment = models.CharField(max_length=1000,null=True,blank=True)
    request_type = models.CharField(max_length=30,choices=LEAD_TYPE,blank=True,null=True)
    lead_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.full_name


class Billing_Details(models.Model):

    report = models.ForeignKey(Report, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50,null=True,blank=True)
    last_name = models.CharField(max_length=50,null=True,blank=True)
    corporate_email = models.EmailField()
    phone = models.CharField(max_length=14,null=True,blank=True)
    company = models.CharField(max_length=50,null=True,blank=True)
    job_title = models.CharField(max_length=50,null=True,blank=True)
    address = models.CharField(max_length=1000,null=True,blank=True)
    city = models.CharField(max_length=20,null=True,blank=True)
    state = models.CharField(max_length=20,null=True,blank=True)
    country = CountryField(blank_label='Country')
    zipcode = models.CharField(max_length=20,null=True,blank=True)
    invoice_date = models.DateField(auto_now_add=True)
    amount =models.CharField(max_length=20,null=True,blank=True)


    class Meta:
        verbose_name_plural = 'BillingDetails'

    def __str__(self):
        return self.first_name + self.last_name

class Contact_Us(models.Model):
    full_name = models.CharField(max_length=50)
    corporate_email = models.EmailField()
    phone = models.CharField(max_length=14)
    subject =models.CharField(max_length=500)
    message = models.TextField()
    contact_date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'ContactUs'

    def __str__(self):
        return self.full_name

class BecomePublisher(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    corporate_email = models.EmailField()
    phone = models.CharField(max_length=14)
    company = models.CharField(max_length=50)
    website = models.URLField()
    intro = models.TextField()
    no_of_report = models.IntegerField()
    yearly_published = models.IntegerField()

    class Meta:
        verbose_name_plural = 'Publisher Partner'

    def __str__(self):
        return self.first_name


class OurClients(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    slug = models.SlugField(blank=True,unique=True)
    image = models.ImageField(upload_to='clients/', blank=True, null=True)
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Our Clients'

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        if not self.slug and self.name:
            self.slug = slugify(self.name)
        super(OurClients,self).save(*args,**kwargs)



