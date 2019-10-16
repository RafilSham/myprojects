from django.shortcuts import render_to_response,redirect,render
from django.template.context_processors import csrf
from django.contrib import auth

def log_in(request):
    '''возвращает шаблон'''
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('login','')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/main/me')
        else:
            args['login_error']  = 'Пользователь не найден'
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html',args)

def log_out(request):
    auth.logout(request)
    return redirect('/auth/login')
