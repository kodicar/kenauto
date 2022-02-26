from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from . models import Contact
from django.conf import settings


# Create your views here.

def contact(request):
  if request.method == 'POST':
    listing_id = request.POST['listing_id']
    listing = request.POST['car']
    name = request.POST['name']
    email = request.POST['email']
    phone = request.POST['phone']
    message = request.POST['message']
    user_id = request.POST['user_id']
    dealer_email = request.POST['email']
    subject = 'New car inquiry'
    email_from = settings.EMAIL_HOST_USER

    #  Check if user has made inquiry already
    if request.user.is_authenticated:
      user_id = request.user.id
      has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
      if has_contacted:
        messages.error(request, 'You have already made an inquiry for this Car')
        return redirect('/cars/'+listing_id)

    contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id )

    contact.save()

    # Send email
    send_mail(subject, message, email_from, [email, settings.D_MAIL, settings.G_MAIL],
      fail_silently=False
    )

    messages.success(request, 'Your request has been submitted, a dealer will get back to you soon')
    return redirect('/cars/'+listing_id)
