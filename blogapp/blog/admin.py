from django.contrib import admin
from .models import Blog, Category
from django.utils.safestring import mark_safe
# Register your models here.

class BlogAdmin(admin.ModelAdmin): # for the screen /admin page on the web browser
    list_display = ("title", "is_active", "is_home", "slug", "selected_categories",)
    list_editable = ( "is_active", "is_home",)
    search_fields = ("title", "description",)
    readonly_fields = ("slug",) # allows us to not edit description on the admin page
    # list_filter = ("category", "is_active", "is_home") # one to many relationship
    list_filter = ("categories", "is_active", "is_home",) # many to many relationship

    def selected_categories(self, obj):
        # html = obj.title
        html = "<ul>" 


        for category in obj.categories.all(): # obj is an Category object contains object properties
            html += "<li>" + category.name + "</li>"

        html += "</ul>"

        return mark_safe(html)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    readonly_fields = ("slug",) # allows us to not edit description on the admin page

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)