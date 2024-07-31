from django.views.generic import TemplateView
from django.contrib import messages
from globals.request_manager import Action
from globals.decorators import GLOBALS
from django.shortcuts import redirect

class RegisterView (TemplateView) :
    template_name = 'register.html'


    def post(self, request) : 
        data = dict(request.POST)
        data.pop('csrfmiddlewaretoken')

        action = Action(
            url=GLOBALS['BACKEND'] + '/user/auth/register/',
            data=data
        )
        action.post()
        if action.is_valid:
            user_token = action.json_data()['access_token']
            response = redirect('home')
            response.set_cookie('user', user_token)
            return response
        
        messages.error(request, 'please enter a valid data')
        return redirect('register')