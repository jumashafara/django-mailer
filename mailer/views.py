from django.core.mail import send_mail
from django.shortcuts import render
from .models import Contact
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.
def sendMail(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            email = form.save()

            send_mail(
                subject=email.subject,
                message=email.message,
                from_email=email.sender_email,
                recipient_list=['jumashafara0@gmail.com'],
            )
            # return success http response
            return HttpResponse('success')
        else:
            context['form': form]
    else:
        context['form'] = ContactForm()
        return render(request=request,
                        template_name='mailer/form.html',
                        context=context)


