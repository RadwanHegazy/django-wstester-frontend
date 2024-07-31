from django.views.generic import TemplateView
from globals.request_manager import Action
from globals.decorators import GLOBALS
from django.shortcuts import redirect
from django.contrib import messages


class LoginView (TemplateView) :
    template_name = 'login.html'


    def post(self, request) : 
        data = dict(request.POST)
        data.pop('csrfmiddlewaretoken')

        action = Action(
            url=GLOBALS['BACKEND'] + '/user/auth/login/',
            data=data
        )
        action.post()
        if action.is_valid:
            user_token = action.json_data()['access_token']
            response = redirect('home')
            response.set_cookie('user', user_token)
            return response
        
        messages.error(request, 'invalid email or password, please try again')
        return redirect('login')