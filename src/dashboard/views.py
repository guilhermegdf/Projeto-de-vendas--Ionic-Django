from django.shortcuts import render
import pyrebase
from FireBaseCredentials import config

firebase = pyrebase.initialize_app(config)

authentic = firebase.auth()
database = firebase.database()
storage = firebase.storage ()
# Create your views here.

def index(request):

    vendas=0
    x = database.child("users").get()
    for i in x.each():
        if str(i.key()) == request.session['uid']:
            request.session['data'] = i.val()

    for key,value in request.session['data']['vendedores'].items():
        if 'vendas' in value:
            vendas = vendas+len(value['vendas'])
    template = 'dashboard.html'
    return render (request,template, {'vendas':vendas})

def users_list(request):
    import datetime
    i = []
    data={}
    template = 'all_users.html'
    users = database.child("users").child(request.session['uid']).child("vendedores").get()

    for x in users.each():
        data[x.key()]=x.val()['details']
    return render(request, template,{'users':data})

def create_user(request):
    template = 'new_users.html'
    return render(request, template, {'users':True})

def pedent_user(request):
    template = 'all_users.html'
    return render(request, template)

def userinfo(request, id):

    user_data = database.child("users").child(request.session['uid']).child("vendedores").child(id).child("details").get().val()
    template = 'new_users.html'
    return render(request, template,{'id':id, 'update':True, 'data':user_data})

def order_list(request):
    template = 'all_users.html'
    vendas = database.child("users").child(request.session['uid']).child("vendedores").get().val()
    return render(request, template, {'order':vendas})

def orderinfo(request, id):

    template = 'new_users.html'
    return render(request, template,{'id':id, 'update':True, 'data':user_data})