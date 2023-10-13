from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.category import Category
from store.models.orders import Order
from store.models.enquiry import EnquiryCat
from store.models.enquiry import CustEnq
from store.middlewares.auth import auth_middleware     

class ContactForm(forms.ModelForm): #inheritance
    class Meta:
        model = CustEnq
        fields = '__all__'
