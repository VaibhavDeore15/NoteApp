from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
post=[
    {'id':1,
    'title':'Shreeman legend ',
    'content':'way to manali'},
    {
    'id':2,
    'title':'welcome to nashik ',
    'content':'we are exploring Nashik'
    },
    {
    'id':3,
    'title':'dolly chai wala',
    'content':'read more...'
    }
]
std=[
    {
    'roll':1,
    'name':'shreeman ',
    'age':28},
    {
    'roll':2,
    'name':'Devil',
    'age':22
    },
    {
    'roll':3,
    'name':'Vaibhav',
    'age':22
    }
]
def home(request):
    html=""
    for po in post:
        html+=f'''
        <div>
        <h1>{po['id']} - {po['title']}</h1>
        <p>{po['content']}</p>
        
        </div>
        <hr>
        '''
    return HttpResponse(html)
# def display(request,id):
    
#     html=""
#     for i in post:
#         if id==i['id']:
#             html+=f'''
#             <div>
#             <h1>{i['id']} - {i['title']}</h1>
#             <p>{i['content']}</p>
                
#             </div>
#             <hr>
#             '''
#             break
#     return HttpResponse(html)

def show(request, roll):
    html = ""

    for i in std:
        if i['roll'] == roll:
            dic = i
            html += f'''
                <div>
                    <h1>{dic['name']}</h1>
                    <p>{dic['age']}</p>
                </div>
                <hr>
            '''
            return HttpResponse(html)

    return HttpResponse('<h1>Name is not found in Record</h1>')

def demo(request):
    Data=data.objects.all()
    # print(Data.name)
    return render(request,'index.html',context={'data':Data})

def savedata(request):
    name=request.POST.get("name")
    msg=request.POST.get("msg")
    Data=data(name=name,msg=msg)
    Data.save()
    return redirect('demo')

def deleteview(request,id):
    Data=data.objects.get(id=id) or None
    Data.delete()
    return redirect('demo')

def updateview(request,id):
    
    Data=data.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get("name","")
        msg=request.POST.get("msg","")
        Data.name=name
        Data.msg=msg
        Data.save()
        return redirect('demo')
    return render(request,'update.html',context={'Data':Data}) 

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request,user)
            return redirect('demo')
    return render(request,'login.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        branch=request.POST['branch']
        User.objects.create_user(username=username, password=password)
        return redirect('login')
    return render(request,'register.html')

def search(request):
    query=request.GET.get('username')
    users=User.objects.filter(username__icontains=users)
    return render(request,"index.html",{"users":users})
