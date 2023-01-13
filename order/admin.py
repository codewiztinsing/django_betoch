from django.contrib import admin
from .models import Order,OrderItem


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
    	"id",
    	"first_name", 
    	"email",
    	"created_at",
    	"paid_amount",
    	
    	)


admin.site.register(OrderItem)
