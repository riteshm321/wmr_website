from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin,ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field
from rangefilter.filter import DateRangeFilter



from .models import (Report, Publisher, Category, SliderImage, Lead,
                     Billing_Details,Contact_Us,BecomePublisher,OurClients)



class ReportResource(resources.ModelResource):
    class Meta:
        model = Report
        fields = ('id','title', 'keyword', 'category', 'publisher','summary','published_date','single_user_price','corporate_user_price')
        # exclude = ('email')

# class ReportResource(resources.ModelResource):
#     publisher = Field()
#     category = Field()
#     class Meta:
#         model = Report
#
#     def dehydrate_publisher(self, report):
#         return report.publisher.name
#
#     def dehydrate_category(self, report):
#         return report.category.name


class ReportAdmin(ImportExportActionModelAdmin):
    # resource_class = ReportResource
    list_display = ['id','title', 'keyword', 'category', 'publisher','url']
    list_select_related = ('category','publisher')
    list_filter = (('published_date',DateRangeFilter),'category', 'publisher')
    # autocomplete_fields = ['title']
    search_fields = ('title',)
    list_display_links = ('id','title')
    list_per_page = 500

class CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'name', 'description', 'slug']
    list_display_links = ('id','name')
    list_per_page = 25


class PublisherAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'name', 'description', 'slug']
    list_display_links = ('id', 'name')


# class ReportAdmin(ImportExportActionModelAdmin):
#     list_display = ['id', 'keyword','title', 'category', 'publisher','url']
#     list_filter = ('category', 'publisher')


class LeadAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'lead_date','report', 'full_name', 'corporate_email', 'country', 'phone', 'job_title', 'company',
                    'comment' ]
    list_display_links = ('id', 'full_name')
    list_per_page = 25

class ContactUsAdmin(ImportExportActionModelAdmin):
    list_display = ['id','full_name', 'corporate_email','phone','subject','message']
    list_display_links = ('id', 'full_name')

class SliderAdmin(admin.ModelAdmin):
    list_display = ['id','image']


admin.site.register(Report,ReportAdmin)
admin.site.register(Publisher,PublisherAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Lead,LeadAdmin)
admin.site.register(SliderImage,SliderAdmin)
admin.site.register(Billing_Details)
admin.site.register(Contact_Us,ContactUsAdmin)
admin.site.register(BecomePublisher)
admin.site.register(OurClients)

admin.site.site_header = 'Wisdom Market Research'
admin.site.site_title = 'Admin | Wisdom Market Research'
admin.site.index_title = 'Admin | Wisdom Market Research'