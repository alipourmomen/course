from django.shortcuts import render, HttpResponse
from django.http import Http404
# database
users = [
    {
        'username': 'dayan',
        'lastname': 'ghanbari',
        'name': 'dayan',
        'phone': '09391231234',
        'city': 'tehran'
    },
    {
        'username': 'mahdi',
        'lastname': 'ghanbarpour',
        'name': 'mahdi',
        'phone': '09391231234',
        'city': 'bushehr'
    },
    {
        'username': 'niki',
       'lastname': 'bagheri',
         'name': 'niki',
        'phone': '09391231234',
        'city': 'hameja'
    },
]

def userslist(request):
    """ users_list => users""" 
    return render(request, 'accounts_app/user_list.html', context={'users_list': users})

def profile(request, username):
    for user in users:
        if user['username'] == username:
            return render(request, 'accounts_app/profile.html', context={'user': user})

    #raise Http404('This user is not exist')
    return HttpResponse('not found page - پیج مورد نظر پیدا نشد')
    

def info(request):
    return render(request, "accounts_app/info.html")
