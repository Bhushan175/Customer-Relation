from django.contrib import admin

from .models import Customer,Products,Orders

class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','mobile','location']

class AdminProducts(admin.ModelAdmin):
    list_display = ['name','price','description','order_date','category']

class AdminOrders(admin.ModelAdmin):
    list_display = ['status','created_date']

admin.site.register(Customer, AdminCustomer)
admin.site.register(Products,AdminProducts)
admin.site.register(Orders,AdminOrders)
