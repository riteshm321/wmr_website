

from django import forms
from .models import Lead,Billing_Details,Contact_Us,BecomePublisher
from django_countries.widgets import CountrySelectWidget



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact_Us
        fields = ['full_name','corporate_email','phone','subject','message']
        widgets ={

            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder' : "  Full Name",
                    'name':'fullname',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'corporate_email': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Email",
                    'name':'email',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Phone No.(Please Affix Country Code)",
                    'name':'phone',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Subject",
                    'name':'subject',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Please specify your requirement to help you with all the research solutions.",
                    'rows': '3',
                    'cols': '40',
                    'name':'comment',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'

                }
            ),
        }

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['full_name','corporate_email','country','phone','job_title','company','comment']
        widgets = {
            'country': forms.Select(
                attrs={
                    'class': 'form-control mb-2',
                    'name': 'country',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'full_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder' : "  Full Name",
                    'name':'fullname',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'corporate_email': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Email",
                    'name':'email',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Phone No.(Please Affix Country Code)",
                    'name':'phone',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'job_title': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Job Title",
                    'name':'job_title',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'company': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Company",
                    'name':'company',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Please specify your requirement to help you with all the research solutions.",
                    'rows': '3',
                    'cols': '40',
                    'name':'comment',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'

                }
            ),
            'message': forms.Textarea(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Message",
                    'rows': '3',
                    'cols': '40',
                    'name': 'message',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'

                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Last Name",
                    'name': 'lastname',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
        }


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Billing_Details
        exclude = ['report']
        widgets = {
            'country': forms.Select(
                attrs={
                    'class': 'form-control mb-2',
                    'name': 'country',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'country'
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  First Name",
                    'name': 'First Name',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'first_name'
                }
            ),
            'corporate_email': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Email",
                    'name': 'email',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'corporate_email'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Phone No.(Please Affix Country Code)",
                    'name': 'phone',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'phone'
                }
            ),
            'job_title': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Job Title",
                    'name': 'job_title',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'job_title'
                }
            ),
            'company': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Company",
                    'name': 'company',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'company'
                }
            ),
            'address': forms.Textarea(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Address",
                    'rows': '3',
                    'cols': '40',
                    'name': 'address',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'address'

                }
            ),
            'city': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  City",
                    'name': 'city',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'city',
                }
            ),
            'state': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  State",
                    'name': 'state',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'state'
                }
            ),
            'zipcode': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Zip Code",
                    'name': 'zipcode',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'zipcode'

                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Last Name",
                    'name': 'lastname',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;',
                    'id': 'last_name'
                }
            )
        }


class BecomePublisherFrom(forms.ModelForm):
    class Meta:
        model = BecomePublisher
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  First Name",
                    'name': 'first_name',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'corporate_email': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Email",
                    'name': 'corporate_email',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'phone': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Phone No.(Please Affix Country Code)",
                    'name': 'phone',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'website': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Company Website",
                    'name': 'website',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'company': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Company",
                    'name': 'company',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'intro': forms.Textarea(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Company Introduction",
                    'rows': '3',
                    'cols': '40',
                    'name': 'intro',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'

                }
            ),
            'no_of_report': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  No. of Reports",
                    'name': 'no_of_report',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'yearly_published': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Yearly Published Report",
                    'name': 'yearly_published',
                    'style': 'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control mb-2',
                    'placeholder': "  Last Name",
                    'name': 'lastname',
                    'style':'border: 1px solid #A9A9A9;border-radius: 4px;'
                }
            )
        }