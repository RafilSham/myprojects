from django.db import models
from login import myFields
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Subject(models.Model):
    class Meta():
        db_table = 'subject'
    name = models.CharField(max_length=100)

    def __str__(self):
        return "%s" % self.name

class Teacher(models.Model):
    class Meta():
        db_table = 'teacher'
    fname = models.CharField(max_length=100)
    sname = models.CharField(max_length=100)
    thname = models.CharField(max_length=100)
    staj = models.PositiveIntegerField()

    def __str__(self):
        return "%s %s %s" % (self.sname,self.fname,self.thname)

class Rasp(models.Model):
    class Meta():
        db_table = 'rasp'
    teacher = models.ForeignKey(Teacher)
    subject = models.ForeignKey(Subject)
    def __str__(self):
        return "%s %s" % (self.subject,self.teacher)

class Clas(models.Model):
    class Meta():
        db_table = 'clas'
    char_class = models.CharField(max_length= 4,primary_key=True)
    classmaster = models.OneToOneField(Teacher)

    def __str__(self):
        return "%s" % (self.char_class)


class Schedule(models.Model):
    class Meta():
        db_table = 'schedule'
        #unique_together = ("_s1", "_s2","_s3", "_s4","_s5", "_s6","_s7", "_s8")
    classes = models.ForeignKey(Clas)
    s1 = models.ForeignKey(Rasp,related_name='rasp_s1',blank=True,null=True)
    s2 = models.ForeignKey(Rasp,related_name='pasp_s2',blank=True,null=True)
    s3 = models.ForeignKey(Rasp, related_name='rasp_s3',blank=True,null=True)
    s4 = models.ForeignKey(Rasp, related_name='pasp_s4',blank=True,null=True)
    s5 = models.ForeignKey(Rasp, related_name='rasp_s5',blank=True,null=True)
    s6 = models.ForeignKey(Rasp, related_name='pasp_s6',blank=True,null=True)
    s7 = models.ForeignKey(Rasp, related_name='rasp_s7',blank=True,null=True)
    s8 = models.ForeignKey(Rasp, related_name='pasp_s8',blank=True,null=True)
    st_day = models.DateField()
    end_day = models.DateField()
    date = myFields.DayOfTheWeekField()
    def __str__(self):
        return "%s %s "% (self.classes,self.date)

from django.conf import settings
class Profile(models.Model):
    class Meta():
        db_table = 'profile'
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    classes = models.ForeignKey(Clas)
    email = models.EmailField(blank=True,null=True)
    img = models.ImageField(blank=True,null=True, upload_to = "profile_img/%Y/%m/%d/")
    def __str__(self):
        return "%s %s %s" % (self.classes, self.user.first_name, self.user.last_name)

class Hw(models.Model):
    class Meta():
        db_table = 'hw'
    value = models.CharField(max_length=100,blank=True,null=True)
    subject = models.ForeignKey(Rasp)
    classes = models.ForeignKey(Clas)
    date = models.DateField()

    def __str__(self):
        return "%s %s %s %s" % (self.date,self.classes,self.subject,self.value)

class Dnevnik(models.Model):
    class Meta():
        db_table = 'dnevnik'
    student = models.ForeignKey(Profile)
    subject = models.ForeignKey(Rasp,default=0)
    value = models.PositiveIntegerField(blank=True,null=True)
    comment = models.TextField(blank=True,null=True)
    date = models.DateField(null=True)
    def __str__(self):
        return "%s" % (self.date)

def user_unicode_patch(self):
    return '%s %s' % (self.first_name, self.last_name)

User.__unicode__ = user_unicode_patch