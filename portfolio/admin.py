from django.contrib import admin
from .models import Contact,Portfolio, Blog, Category,Comment,Gallery,Book,PortfolioCategory,GalleryCategory,Portfolio_single
from django.utils.html import format_html

# Register your models here.
admin.site.register((Comment,Category,PortfolioCategory,GalleryCategory,Portfolio_single))

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email')

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title','description')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('img','title','category_name')
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}"style="border-radius: 50%;" />'.format(obj.image.url))

    def category_name(self, obj):
        return obj.category.name
    #rasmni ko'rinadigan qilasilar


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('img', 'title', 'created_date')
    readonly_fields = ['id']

    def img(self, obj):
        return format_html(
            '<img width="100" height="100" src="{}" style="border-radius: 50%;" />',
            obj.image.url
        )

@admin.register(Book)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('img','title','author','description','description','pages','publication_date','publisher')
    readonly_fields = ['id']
    def img(self, obj):
         return format_html('<img width="100" height="100" src="{}" />'.format(obj.cover.url))
  
