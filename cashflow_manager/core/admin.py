from django.contrib import admin
from .models import Status, Type, Category, Subcategory, Transaction


admin.site.register(Status)
admin.site.register(Type)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'type')


@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('date', 'status', 'type', 'category', 'subcategory', 'amount', "comment")
    list_filter = ('date', 'status', 'type', 'category', 'subcategory')
