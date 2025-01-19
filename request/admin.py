from django.contrib import admin
from .models import CustomerRequest

@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'customer_email', 'customer_phone', 'customer_address', 'issue_description', 'status', 'created_at', 'tentative_date', 'resolved_at']
    list_filter = ['status']
    search_fields = ['customer_name', 'customer_email']
