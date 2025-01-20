from django.db import models
import uuid

class CustomerRequest(models.Model):
    customer_name = models.CharField(max_length=255)  # Name of the customer
    customer_email = models.EmailField()             # Email of the customer
    customer_phone = models.CharField(max_length=15) # Phone number of the customer
    customer_address = models.TextField()            # Address of the customer
    issue_description = models.TextField()           # Description of the issue
    status = models.CharField(
        max_length=50,
        choices=[('Pending', 'Pending'), ('In Progress', 'In Progress'), ('Resolved', 'Resolved')],
        default='Pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)  # When the request was created
    tentative_date = models.DateField(null=True, blank=True)  # Tentative resolution date
    resolved_at = models.DateTimeField(null=True, blank=True)  # Resolution timestamp

    tracking_id = models.UUIDField(default=uuid.uuid4, editable=False)  # Remove unique=True
    
    def __str__(self):
        return self.customer_name



from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import CustomerRequest

@receiver(post_save, sender=CustomerRequest)
def notify_customer_on_update(sender, instance, created, **kwargs):
    if not created:  # Only for updates, not new submissions
        send_mail(
            'Your Issue Update',
            f"Dear {instance.customer_name},\n\nYour issue status has been updated to '{instance.status}'. "
            f"The tentative resolution date is {instance.tentative_date}.\n\nThank you,\nGas Utility Support Team",
            'support@gasutility.com',  # Sender email
            [instance.customer_email],  # Recipient email
            fail_silently=False,
        )