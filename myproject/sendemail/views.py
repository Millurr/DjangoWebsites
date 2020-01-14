from django.shortcuts import render, redirect
from django.views.generic import View
from django.template import loader 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

def emailView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, 'postmaster@sandboxe883356e500b44608ecd89a6f9e4f335.mailgun.org', ['josh.miller@selu.edu'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, 'sendemail/email.html', {'form':form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

