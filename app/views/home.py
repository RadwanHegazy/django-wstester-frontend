from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views import View
from globals.decorators import login_required
from django.shortcuts import render

class HomeView (View) :

    @login_required
    def get(self, request, **kwargs):
        return render(request,'home.html')