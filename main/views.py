from django.shortcuts import render_to_response,redirect,render
from django.contrib import auth
from django.template.context_processors import csrf
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from login import models
import datetime
import calendar
from django.template.defaultfilters import date

dicts = {}
def show(request):
    '''возвращает шаблон'''
    if request.user.is_authenticated():
        dnevnik(request,dicts)
        return render_to_response('dnevnik.html',dicts)
    else:
        return redirect('/auth/login')
        # Анонимный пользователь. Перекидываем обратно на страницу авторизации

dates = {'Monday':'Понедельник','Tuesday':'Вторник','Wednesday':'Среда','Thursday':'Четверг','Friday':'Пятница',
         'Saturday':'Суббота','Sunday':'Воскресенье'}

def dnevnik(request,dicts):
    if request.GET:
        if request.GET.get('date', '')!='':
            dicts['date'] = request.GET.get('date', '')
        else:
            dicts['date'] = datetime.date.today().strftime("%Y-%m-%d")
    else:
        dicts['date'] = datetime.date.today().strftime("%Y-%m-%d")
    # Пользователь авторизован.
    day = dicts['date'].split('-')
    dotw= datetime.date(int(day[0]),int(day[1]),int(day[2])).weekday() + 1
    my_day = dates[str(calendar.day_name[dotw-1])] #перевод на русский
    # id + name ученика
    id_stud = models.Profile.objects.get(user=auth.get_user(request).id)
    #id_stud = id_stud.classes
    # id classa к которому принадлежит ученик
    id_class = models.Clas.objects.get(char_class=id_stud.classes)

    #Вывод расписания на 1 день для конкретного класса
    try:
        sched = models.Schedule.objects.get(date=dotw,classes=id_class)
        sched.end_day=sched.end_day.strftime("%Y-%m-%d")
        sched.st_day=sched.st_day.strftime("%Y-%m-%d")
    except:
        sched = ''

    #Вывод оценок за этот день
    try:
        values = models.Dnevnik.objects.filter(date = dicts['date'],student=id_stud)
    except:
        values =''

    try:
        homeworks = models.Hw.objects.filter(date=dicts['date'],classes=id_class)
    except:
        homeworks =''
    dicts['fname'] = auth.get_user(request).first_name #Имя
    dicts['sname'] = auth.get_user(request).last_name #Фамилия
    dicts['sched'] = sched
    dicts['weekday']=my_day
    dicts['id_cl']=id_class
    dicts['values'] = values #оценки
    dicts['homeworks'] = homeworks
    pass

from login.forms import ProfileForm,ImageUploadForm

@login_required
def profile(request):
    dicts['profile'] = models.Profile.objects.get(user=auth.get_user(request).id)
    dicts['form'] = ProfileForm(request.POST or None,instance = dicts['profile'])
    return render(request,'profile.html',dicts)

@login_required
def profile_save(request):
    try:
        profile = models.Profile.objects.get(user=auth.get_user(request).id)
        if request.POST:
            form = ImageUploadForm(request.POST, request.FILES)
            profile.email = request.POST.get('email', '')
            profile.save()
            if form.is_valid():
                profile.img = form.cleaned_data['image']
                profile.save()
            return redirect('/main/profile',dicts)
        else:
            return redirect('/main/profile',dicts)
    except profile.DoesNotExist:
        return HttpResponseNotFound("<h2>Пользователь не найден</h2>")

from itertools import chain
def values(request):
    args={}
    id_stud = models.Profile.objects.get(user=auth.get_user(request).id)
    # id_stud = id_stud.classes
    # id classa к которому принадлежит ученик
    all_subs = models.Rasp.objects.all()
    id_class = models.Clas.objects.get(char_class=id_stud.classes)
    s1 = models.Schedule.objects.filter(classes=id_class).values_list('s1',flat=True).distinct()
    s2 = models.Schedule.objects.filter(classes=id_class).values_list('s2', flat=True).distinct()
    s3 = models.Schedule.objects.filter(classes=id_class).values_list('s3', flat=True).distinct()
    s4 = models.Schedule.objects.filter(classes=id_class).values_list('s4', flat=True).distinct()
    s5 = models.Schedule.objects.filter(classes=id_class).values_list('s5', flat=True).distinct()
    s6 = models.Schedule.objects.filter(classes=id_class).values_list('s6', flat=True).distinct()
    list=[]

    report = chain(s1,s2,s3,s4,s5,s6) #Объединение запросов
    for all_subs in report:
        try:
            list.append(models.Rasp.objects.get(id=all_subs))
        except:
            err = 'error'
    list = set(list)

    d = {}
    vals = models.Dnevnik.objects.filter(student=id_stud)
    for x in list:
        s=0
        i=0
        for y in vals:
            if x==y.subject:
                s=s+y.value
                i=i+1
        if i>2:
            d.update({x:s/i})
        else:
            d.update({x:0})

    #s1 = models.Schedule.objects.filter(classes=id_class).order_by('s1').distinct()
    return render_to_response('values.html',{'values':d})