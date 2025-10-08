from django.contrib import admin
from .models import Customer,Student,Author
from .form import ContactForm,CustomerForm,StudentForm
# Register your models here.
#One of the most powerful parts of Django is the automatic admin interface. It reads metadata from your models to provide a quick, model-centric interface where trusted users can manage content on your site. The admin’s recommended use is limited to an organization’s internal management tool. It’s not intended for building your entire front end around.
#https://docs.djangoproject.com/en/5.2/ref/contrib/admin/#hooking-adminsite-to-urlconf
#Above is the documentation for the admin site

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    pass
#This attribute overrides the default display value for record’s fields that are empty (None, empty string, etc.).
class AuthorAdmin(admin.ModelAdmin):
    empty_value_display = "-empty-"


#You can also override empty_value_display for all admin pages with AdminSite.empty_value_display, or for specific fields like this:
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name"]
    form=CustomerForm## Admin forms

    @admin.display(empty_value="???")
    def view_firsr_name(self, obj):
        return obj.first_name


class AuthorAdmin(admin.ModelAdmin):
    fields = ["name", "title"]

#we can use both ways to exclude any field from the 
#class AuthorAdmin(admin.ModelAdmin):
    #exclude = ["birth_date"]

#Use the fields option to make simple layout changes in the forms on the “add” and “change” pages such as showing only a subset of available fields, modifying their order, or grouping them into rows

#example
class FlatPageAdmin(admin.ModelAdmin):
    fields = ["url", "title", "content"]

#To display multiple fields on the same line, wrap those fields in their own tuple. In this example, the url and title fields will display on the same line and the content field will be displayed below them on its own line:

# class FlatPageAdmin(admin.ModelAdmin):
#     fields = [("url", "title"), "content"]

#fieldsets:fieldsets is a list of 2-tuples, in which each 2-tuple represents a <fieldset> on the admin form page. (A <fieldset> is a “section” of the form.)
#The 2-tuples are in the format (name, field_options), where name is a string representing the title of the fieldset and field_options is a dictionary of information about the fieldset, including a list of fields to be displayed in it.
# class FlatPageAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (
#             None,#name
#             {
#                 "fields": ["url", "title", "content", "sites"],#fileds
#             },
#         ),
#         (
#             "Advanced options",
#             {
#                 "classes": ["collapse"],
#                 "fields": ["registration_required", "template_name"],
#             },
#         ),
#     ]
#A list or tuple containing extra CSS class to apply to filed set can also be added
#Example:
# {
#     "classes": ["wide", "collapse"],
# }