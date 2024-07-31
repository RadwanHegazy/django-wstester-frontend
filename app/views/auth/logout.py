from django.views.generic import View
from django.shortcuts import redirect

class LogoutView (View) :
    def get(self ,request) : 
        response = redirect('login')
        response.delete_cookie('user')
        return response