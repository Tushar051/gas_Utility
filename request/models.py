# from django.db import models
# from django.utils import timezone

# class CustomerRequest(models.Model):
#     STATUS_CHOICES = [
#         ('submitted', 'Submitted'),
#         ('approved', 'Approved'),
#         ('resolved', 'Resolved'),
#     ]
    
#     customer_name = models.CharField(max_length=100)
#     customer_email = models.EmailField()
#     customer_phone = models.CharField(max_length=15)
#     customer_address = models.CharField(max_length=255)
#     issue_description = models.TextField()
#     status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='submitted')
#     created_at = models.DateTimeField(default=timezone.now)
#     approved_at = models.DateTimeField(null=True, blank=True)
#     resolved_at = models.DateTimeField(null=True, blank=True)

#     def __str__(self):
#         return f"Request from {self.customer_name} ({self.status})"


from django.db import models

class CustomerRequest(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    customer_address = models.TextField(null=True, blank=True)
    issue_description = models.TextField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tentative_date = models.DateField(null=True, blank=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.customer_name} - {self.status}"
