# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.mail import send_mail

from .forms import ContactForm

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                data['subject'],
                data['content'],
                '', #FROM
                [data['email']],
                fail_silently=False,
            )
            return HttpResponseRedirect('/feedback/thanks/')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

def thanks(request):
    return render(request, 'thanks.html')
