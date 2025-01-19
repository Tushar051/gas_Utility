from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import CustomerRequest

@receiver(post_save, sender=CustomerRequest)
def send_status_update_email(sender, instance, **kwargs):
    if not kwargs['created']:  # Update only, not creation
        send_mail(
            subject="Issue Status Update",
            message=f"Hello {instance.customer_name},\n\nYour issue status has been updated to '{instance.status}'. The tentative resolution date is {instance.tentative_date}.",
            from_email="support@gasutility.com",
            recipient_list=[instance.customer_email],
            fail_silently=False
        )
