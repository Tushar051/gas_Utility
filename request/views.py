from datetime import timezone
from django.shortcuts import render, redirect
from .forms import CustomerRequestForm
from .models import CustomerRequest
from django.core.mail import send_mail
from django.conf import settings


from django.shortcuts import render

def home(request):
    return render(request, 'home.html')  # This will render the home.html template


# Customer request form page
def customer_request(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            # Save the customer request
            customer_request = form.save()
            
            # Send the tracking ID to the customer email
            send_mail(
                'Your Tracking ID',
                f'Your tracking ID is {customer_request.id}. You can track the status of your issue.',
                settings.DEFAULT_FROM_EMAIL,
                [customer_request.customer_email],
            )
            return redirect('thank_you')
    else:
        form = CustomerRequestForm()
    return render(request, 'customer_request.html', {'form': form})

# Thank you page after form submission
def thank_you(request):
    return render(request, 'thank_you.html')

# Admin view to approve/resolve requests
def admin_dashboard(request):
    requests = CustomerRequest.objects.all()
    return render(request, 'admin_dashboard.html', {'requests': requests})

# Admin view to update request details
def update_request(request, request_id):
    customer_request = CustomerRequest.objects.get(id=request_id)
    if request.method == 'POST':
        customer_request.status = request.POST['status']
        if 'approved_at' in request.POST:
            customer_request.approved_at = timezone.now()
        if 'resolved_at' in request.POST:
            customer_request.resolved_at = timezone.now()
        customer_request.save()

        # Send email to customer about the update
        send_mail(
            'Your Issue Status Update',
            f'Your issue has been updated to {customer_request.status}. Tentative resolution date: {customer_request.resolved_at}',
            settings.DEFAULT_FROM_EMAIL,
            [customer_request.customer_email],
        )

        return redirect('admin_dashboard')
    return render(request, 'update_request.html', {'request': customer_request})


from django.shortcuts import render, redirect
from .forms import CustomerRequestForm

def submit_request(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form to the database
            return render(request, 'success.html')  # Redirect to a success page
    else:
        form = CustomerRequestForm()  # Initialize a blank form
    return render(request, 'submit.html', {'form': form})


def home(request):
    return render(request, 'home.html')

from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    try:
        send_mail(
            'Test Email Subject',
            'This is a test email.',
            'your_email@gmail.com',
            ['recipient_email@example.com'],
            fail_silently=False,
        )
        return HttpResponse("Email sent successfully!")
    except Exception as e:
        return HttpResponse(f"Error: {str(e)}")
