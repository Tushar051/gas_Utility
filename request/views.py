from datetime import timezone
from django.shortcuts import render, redirect
from .forms import CustomerRequestForm
from .models import CustomerRequest
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, get_object_or_404

def home(request):
    return render(request, 'home.html')  # This will render the home.html template


def customer_request(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            customer_request = form.save()
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


def thank_you(request):
    return render(request, 'thank_you.html')

def admin_dashboard(request):
    requests = CustomerRequest.objects.all()
    return render(request, 'admin_dashboard.html', {'requests': requests})

def update_request(request, request_id):
    customer_request = CustomerRequest.objects.get(id=request_id)
    if request.method == 'POST':
        customer_request.status = request.POST['status']
        if 'approved_at' in request.POST:
            customer_request.approved_at = timezone.now()
        if 'resolved_at' in request.POST:
            customer_request.resolved_at = timezone.now()
        customer_request.save()

        send_mail(
            'Your Issue Status Update',
            f'Your issue has been updated to {customer_request.status}. Tentative resolution date: {customer_request.resolved_at}',
            settings.DEFAULT_FROM_EMAIL,
            [customer_request.customer_email],
        )

        return redirect('admin_dashboard')
    return render(request, 'update_request.html', {'request': customer_request})


def submit_request(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            form.save()  
            return render(request, 'success.html')  
    else:
        form = CustomerRequestForm() 
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

def submit_request(request):
    if request.method == 'POST':
        form = CustomerRequestForm(request.POST)
        if form.is_valid():
            customer_request = form.save()
            
           
            subject = 'Your Service Request Has Been Submitted'
            message = f"""
                Hello {customer_request.customer_name},
                
                Your request has been received and is currently being processed.
                
                Tracking ID: {customer_request.tracking_id}
                Description: {customer_request.issue_description}
                
                You can track your request at:
                http://127.0.0.1:8000/track/?id={customer_request.tracking_id}
            """
            from_email = 'your_email@example.com'
            recipient_list = [customer_request.customer_email]
            
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            return render(request, 'success.html', {'tracking_id': customer_request.tracking_id})
    else:
        form = CustomerRequestForm()
    
    return render(request, 'submit_request.html', {'form': form})




def track_request(request):
    tracking_id = request.GET.get('id')
    if not tracking_id:
        return render(request, 'track.html', {'error': 'Tracking ID is required.'})
    
   
    request_obj = get_object_or_404(CustomerRequest, tracking_id=tracking_id)
    
    return render(request, 'track.html', {'request_obj': request_obj})
