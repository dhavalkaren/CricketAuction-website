from django.shortcuts import render,get_object_or_404,redirect
from .models import cricketer,MI,CSK,RCB,SRH,KKR,KXIP,DC,RR
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail

# Create your views here.
def login(request):
    return render(request,"login.html")
def verify(request):
    if request.method== 'POST':
        username=request.POST['uname']
        password=request.POST['pass']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect("home")
        else:
            return redirect("login")
    else:
        return render(request,"login.html")
def bid(request,name):
    cricketers = cricketer.objects.get(cricketer_name=name)
    cricketers.bid=str(int(cricketers.bid)+1000000)
    cricketers.save()
    nm = request.user.username
    mi = MI.objects.all()
    csk = CSK.objects.all()
    rcb = RCB.objects.all()
    srh = SRH.objects.all()
    kkr = KKR.objects.all()
    rr = RR.objects.all()
    kxip = KXIP.objects.all()
    dc = DC.objects.all()
    if(nm=='MI'):
        for lists in csk:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in mi:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in srh:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rcb:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kkr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in dc:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kxip:
            if lists.cricketer_name==str(name):
                lists.delete()
        new = MI.objects.create()
        new.cricketer_name=str(name)
        new.bid=str(int(cricketers.bid))
        new.image=cricketers.image.url
        new.save()
    if(nm=='CSK'):
        for lists in csk:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in mi:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in srh:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rcb:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kkr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in dc:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kxip:
            if lists.cricketer_name==str(name):
                lists.delete()
        new = CSK.objects.create()
        new.cricketer_name=str(name)
        new.bid=str(int(cricketers.bid))
        new.image=cricketers.image.url
        new.save()
    if(nm=='RCB'):
        for lists in csk:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in mi:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in srh:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rcb:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kkr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in dc:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kxip:
            if lists.cricketer_name==str(name):
                lists.delete()
        new = RCB.objects.create()
        new.cricketer_name=str(name)
        new.bid=str(int(cricketers.bid))
        new.image=cricketers.image.url
        new.save()
    if(nm=='SRH'):
        for lists in csk:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in mi:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in srh:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rcb:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kkr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in dc:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kxip:
            if lists.cricketer_name==str(name):
                lists.delete()
        new = SRH.objects.create()
        new.cricketer_name=str(name)
        new.bid=str(int(cricketers.bid))
        new.image=cricketers.image.url
        new.save()
    if(nm=='KKR'):
        for lists in csk:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in mi:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in srh:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rcb:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kkr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in dc:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kxip:
            if lists.cricketer_name==str(name):
                lists.delete()
        new = KKR.objects.create()
        new.cricketer_name=str(name)
        new.bid=str(int(cricketers.bid))
        new.image=cricketers.image.url
        new.save()
    if(nm=='KXIP'):
        for lists in csk:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in mi:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in srh:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rcb:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kkr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in dc:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kxip:
            if lists.cricketer_name==str(name):
                lists.delete()
        new = KXIP.objects.create()
        new.cricketer_name=str(name)
        new.bid=str(int(cricketers.bid))
        new.image=cricketers.image.url
        new.save()
    if(nm=='DC'):
        for lists in csk:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in mi:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in srh:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rcb:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kkr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in dc:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kxip:
            if lists.cricketer_name==str(name):
                lists.delete()
        new = DC.objects.create()
        new.cricketer_name=str(name)
        new.bid=str(int(cricketers.bid))
        new.image=cricketers.image.url
        new.save()
    if(nm=='RR'):
        for lists in csk:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in mi:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in srh:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rcb:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kkr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in rr:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in dc:
            if lists.cricketer_name==str(name):
                lists.delete()
        for lists in kxip:
            if lists.cricketer_name==str(name):
                lists.delete()
        new = RR.objects.create()
        new.cricketer_name=str(name)
        new.bid=str(int(cricketers.bid))
        new.image=cricketers.image.url
        new.save()
    return redirect("viewall")

def home(request):
    return render(request,"home.html")

def viewteam(request):
    nm = request.user.username
    if(nm=='MI'):
        all = MI.objects.all()
    if(nm=='CSK'):
        all = CSK.objects.all()
    if(nm=='RCB'):
        all = RCB.objects.all()
    if(nm=='SRH'):
        all = SRH.objects.all()
    if(nm=='KKR'):
        all = KKR.objects.all()
    if(nm=='KXIP'):
        all = KXIP.objects.all()
    if(nm=='RR'):
        all = RR.objects.all()
    if(nm=='DC'):
        all = DC.objects.all()
    return render(request,"viewteam.html",{'all':all})

def logout(request):
    return render(request,"login.html")

def sendmail(request):
    subject = request.POST['Subject']
    message =request.POST['Message']
    email =request.POST['Email']
    finalmessage="Subject: "+subject+"\nFrom: "+email+"\nMessage: "+message

    if(send_mail('A Message From cricket Auction Website', finalmessage, 'dhavalkaren2014@gmail.com', ['dhavalkaren2014@gmail.com'])):
        return render(request,"home.html")
    

    

def viewall(request):
    cricketers = cricketer.objects.all()
    return render(request,"viewall.html",{'cricketers':cricketers})
def profile(request,name):
    cricketers = get_object_or_404(cricketer,cricketer_name=name)
    c_n=cricketers.cricketer_name
    cr= cricketer.objects.all().filter(cricketer_name=c_n)
    return render(request,'profile.html',{'n':cr})



