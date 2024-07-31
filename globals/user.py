from .request_manager import Action
from .decorators import GLOBALS

def userTemp (request) : 

    context = {}
    user = request.COOKIES.get('user',None)
    
    if user is not None :
        headers = {'Authorization':f"Bearer {user}"}
        action = Action(
            url = GLOBALS['BACKEND'] + GLOBALS['PROFILE'],
            headers=headers
        )

        action.get()

        if action.is_valid : 
            context['c_user'] = action.json_data()
    context['main_url'] = GLOBALS['BACKEND']
            
    return context