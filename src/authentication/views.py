from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import auth
import pyrebase
import uuid
from FireBaseCredentials import config
import os.path
# Create your views here.

firebase = pyrebase.initialize_app(config)

authentic = firebase.auth()
database = firebase.database()
storage = firebase.storage ()

def login(request):
    template = 'signIn.html'
    return render (request,template)

def postsign(request):
    email=request.POST.get('email')
    passw = request.POST.get("pass")

    try:
        user = authentic.sign_in_with_email_and_password(email,passw)

    except:
        message="invalid credentials"
        return render(request,"signIn.html",{"invalid":message})
    
    users = database.child("users").get().val()
    session_id=user['localId']
    request.session['uid']=str(session_id)
    request.session['email'] = email
    request.session['img'] = storage.child(request.session['uid']).child('profile.jpeg').get_url('e3b50648-75aa-4b56-9eb0-ec12c22893e5')
    
    

    return redirect ('/index/')

def logout(request):
    auth.logout(request)
    template = 'signIn.html'
    return render(request,template)

def postsignup(request):

    name=request.POST.get("name")
    email = request.POST.get("email")
    passw = request.POST.get("password")
    tip = request.POST.get("type")
    # url = request.POST.get("url")
    try:
        user = authentic.create_user_with_email_and_password(email,passw)
    except:
        template = 'new_users.html'
        return render(request, template, {"message":"Email já cadastrado!"})
    
    user_email = authentic.send_password_reset_email(email)
    uid = user['localId']
    data = {"name": name,"email":email, "type":tip}
    # storage.child(uid).put(myFile)
    if tip == "Vendedor":
        database.child("users").child(request.session['uid']).child("vendedores").child(uid).child("details").set(data)
    
    elif tip =="Franqueado":
        database.child("users").child(uid).child("details").set(data)

    template = 'new_users.html'
    return render(request, template, {"message":"Usuário cadastado com sucesso!"})

def postputuser(request, id):
    data={'name':request.POST.get("name")}
    database.child("users").child(request.session['uid']).child("vendedores").child(id).child("details").update(data)
    
    return redirect('/all_users/')