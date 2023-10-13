from store.forms import ContactForm
from django.shortcuts import render, redirect,  HttpResponseRedirect
from django.contrib.auth.hashers import check_password
import requests
from store.models.customer import Customer
from django.views import View
from django import forms
from store.models.product import Products
from store.models.enquiry import EnquiryCat
from store.models.enquiry import CustEnq
from store.models.orders import Order

from store.middlewares.auth import auth_middleware
    
def contact_name_view(request):
    form = ContactForm()
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid:
            form.save(commit=True)
            return redirect ('homepage')
        else:
            print('Invalid form')
    return render(request, 'contact.html', {'form':form})

   