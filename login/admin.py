from django.contrib import admin
from .models import *
'''регистрируем рользователей'''

class ProfileAdmin(admin.ModelAdmin):
    list_filter = ['classes']
    class Meta:
        model = Profile

class RaspAdmin(admin.ModelAdmin):
    list_filter = ['subject']
    class Meta:
        model = Rasp

class ScheduleAdmin(admin.ModelAdmin):
    list_filter = ['classes']
    list_display = ['classes','date']
    class Meta:
        model = Schedule

class DnevnikAdmin(admin.ModelAdmin):
    list_filter = ['date','student']
    list_display = ['student','subject','value','date']
    class Meta:
        model = Dnevnik

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Rasp,RaspAdmin)
admin.site.register(Teacher)
admin.site.register(Schedule,ScheduleAdmin)
admin.site.register(Subject)
admin.site.register(Clas)
admin.site.register(Hw)
admin.site.register(Dnevnik,DnevnikAdmin)