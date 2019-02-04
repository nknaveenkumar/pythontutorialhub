from django.shortcuts import HttpResponse
from .models import Newsletter
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def sbscription(request):
    email = request.POST.get('email')
    print(email)

    if Newsletter.objects.all().filter(email=email).exists():
        msg = "Email address already exist in datsbase"

    else:
        saveemail = Newsletter(email=email)
        saveemail.save()
        msg = "You have successfully Subscribe..."

        subject = "Thank you for Joining Our Newsletter"
        from_email = settings.EMAIL_HOST_USER
        to_email = [email]
        signup_message = """ Welcome to Joblisting Job portal To search all fields job anywhere  http://localhost:8000/signup/login """
        send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message,
                  fail_silently=False)

    return HttpResponse(msg)