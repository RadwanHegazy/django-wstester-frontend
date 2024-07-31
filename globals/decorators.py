from django.shortcuts import redirect
from .request_manager import Action
from django.conf import settings

GLOBALS = {
    'BACKEND' : 'http://127.0.0.1:4444',
    'PROFILE' : '/user/profile/',
    'LOGIN_REDIRECT' : 'login'
}

try : 
    USER_GLOBALS = settings.GLOBALS
    GLOBALS = {
        **GLOBALS,
        **USER_GLOBALS
    }
except Exception as error :
    print("an error accoured in globals/decorators.py : ", str(error))

def login_required (function) : 

    def wrapper (self, request, **kwargs) : 

        user = request.COOKIES.get('user',None)

        if user is None :
            return redirect(GLOBALS['LOGIN_REDIRECT'])
        
        action = Action(
            url = GLOBALS['BACKEND'] + GLOBALS['PROFILE'],
            headers = {'Authorization':f"Bearer {user}"}
        )

        action.get()

        if not action.is_valid : 
            return redirect(GLOBALS['LOGIN_REDIRECT'])

        kwargs['headers'] = {'Authorization':f"Bearer {user}"}
        kwargs['user'] = action.json_data()
        
        func = function(self,request,**kwargs)
        return func
    
    return wrapper
