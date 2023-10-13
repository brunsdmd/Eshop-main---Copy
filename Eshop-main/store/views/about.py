from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware

class About(View):

    def get(self, request):
        about_text = "About Our Company"
        return render(request, 'about.html', {'about_text': about_text})
