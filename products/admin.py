from django.contrib import admin
from .models import Category, SubCategory, Product, Order, ImageUpload, Cart


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class OrderAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'owner', 'phone_number',
                    'location', 'status', 'date_placed']
    search_fields = ('status', 'date_placed')


admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(ImageUpload)
admin.site.register(Cart)

