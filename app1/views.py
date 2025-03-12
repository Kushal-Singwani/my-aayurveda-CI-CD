from django.shortcuts import render,HttpResponse,redirect
from  app1.models import userclient,adminuser,user_query
from django.contrib.auth import get_user
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    user_id = request.session.get('id')
    print(user_id)
    if user_id:
        user = userclient.objects.get(id=user_id)
        loguser={'user':user}
        return render(request,"index.html",loguser)
    return render(request,"index.html")
def blog(request):
    return render(request,"blog.html")
def service(request):
    return render(request,"service.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")

#login client 
def userlogin(request):
    if request.user.is_authenticated:
        # Agar user login hai, toh homepage ya kisi aur page par redirect karein
        return redirect(home)
    if request.method == "POST":
        email=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user = userclient.objects.filter(email=email, password=password).first()
            if user:
        # Set session data
                request.session['id'] = user.id
                request.session['email'] = user.email 
                return redirect(home)
            else:
                 HttpResponse("Invalid credentials.")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
    return render(request,"login.html")
def Register(request):
    if request.method == "POST":
        name=request.POST.get("username")
        number=request.POST.get("number")
        email=request.POST.get("email")
        password1=request.POST.get("password1")
        password2=request.POST.get("password2")
        if password1 == password2:
            password=password1
            user=userclient.objects.create(name=name,phone=number,email=email,password=password)
            user.save()
            return redirect(userlogin) 
        else:
            return HttpResponse("password is not match")
    return render(request,"register.html")

def log_out(request):
    request.session.flush()  
    return redirect(userlogin)


# client profile panal

def clienthome(request):
    data=request.session.get('id')
    user=userclient.objects.get(id=data)
    print(user)
    return render(request,"clientpenal/index.html",{'user':user})

def payment_info(request):
    data=request.session.get('id')
    user=userclient.objects.get(id=data)
    return render(request,"clientpenal/payment-info.html",{'user':user})

def profile(request):
    data=request.session.get('id')
    user=userclient.objects.get(id=data)
    return render(request,"clientpenal/profile.html",{'user':user})

def document(request):
    data=request.session.get('id')
    user=userclient.objects.get(id=data)
    return render(request,"clientpenal/send-document.html",{'user':user})

def view_suggestion(request):
    data=request.session.get('id')
    user=userclient.objects.get(id=data)
    data=adminuser.objects.all()
    return render(request,"clientpenal/view_suggestion.html",{'user':user,'data':data})

def send_query(request):
    data=request.session.get('id')
    user=userclient.objects.get(id=data)
    if request.method == "POST":
        email=request.POST.get("email")
        query=request.POST.get("query")
        user=user_query.objects.create(Q_email=email,query=query)
        user.save()
        return redirect(send_query)
    return render(request,"clientpenal/send-query.html",{'user':user})

def user_edit(request,id):
    data=userclient.objects.get(pk=id)
    if request.method == "POST":
        data.name=request.POST.get("name")
        data.phone=request.POST.get("number")
        data.email=request.POST.get("email")
        data.password=request.POST.get("password")
        data.save()
        return redirect(profile)
    return render(request,"clientpenal/profile1.html",{'data':data})

# admin profile pages
def pages_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        try:
            user = adminuser.objects.filter(username=username, password=password).first()
            if user:
        # Set session data
                request.session['id'] = user.id
                request.session['username'] = user.username 
                return redirect(adminhome)
            else:
                 HttpResponse("Invalid credentials.")
        except Exception as e:
            return HttpResponse(f"Error: {e}")
        
    return render(request,"admin/pages-login.html")

def adminhome(request):
    data=request.session.get('id')
    user=adminuser.objects.get(id=data)
    return render(request,"admin/index2.html",{'user':user})

def client_profile(request):
    data=request.session.get('id')
    user=adminuser.objects.get(id=data)
    data=userclient.objects.all()
    return render(request,"admin/client-profile.html",{'user':user,'show':data})


def send_suggestions(request):
    data=request.session.get('id')
    user1=adminuser.objects.get(pk=data)
    user=adminuser.objects.get(id=data)
    if request.method == "POST":
        suggestion=request.POST.get("suggestion")
        user1.suggestion=suggestion
        user1.save()      
    return render(request,"admin/send-suggestions.html",{'user':user})

def admin_profile(request):
    data=request.session.get('id')
    user=adminuser.objects.get(id=data)
    return render(request,"admin/users-profile.html",{'user':user})

def view_documents(request):
    data=request.session.get('id')
    user=adminuser.objects.get(id=data)
    return render(request,"admin/view-documents.html",{'user':user})

def view_receive_payment(request):
    data=request.session.get('id')
    user=adminuser.objects.get(id=data)
    return render(request,"admin/view-receive-payment.html",{'user':user})

def view_suggestions(request):
    data=request.session.get('id')
    user=adminuser.objects.get(id=data)
    query=user_query.objects.all()
    print(query)
    return render(request,"admin/view-suggestions.html",{'user':user,'data':query})

def admin_log_out(request):
    request.session.flush()  
    return redirect(pages_login)
def delete(request,id):
    data=userclient.objects.get(pk=id)
    data.delete()
    return redirect(client_profile)
def update(request,id):
    return redirect(client_profile)
