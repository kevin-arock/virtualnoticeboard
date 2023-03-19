from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from .models import MkPost

from django.contrib import messages
from django.contrib.auth import authenticate 
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
import os



def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('date'):
                
                title= request.POST['title']
                date= request.POST['date']
                time= request.POST['time']
                img= request.FILES['pics']
                MkPost.objects.create(title=title,date=date,time=time,img=img)
                

            
            return redirect('admin@post')  

        else:
                return render(request,'post/createpost.html')



def home(request):
    
    post = MkPost.objects.all()
    if request.method == "POST":
        item = request.POST.get('search')
        post = MkPost.objects.filter(title__contains=item) 
        context = {'posts':post}
        return render(request,'mkce/posts.html',context)
    
    context = {"posts":post}
    return render(request,'mkce/posts.html',context)
    
    
    

def login(request):
    
    
    flag=2
    context={'flag':flag}
    if request.method == 'POST': 
        
        username = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            auth_login(request, user)
        # Redirect to a success page.
            return redirect('admin@post') 
        
        else:
            messages.error(request, 'invalid username or password')
            return redirect('login')
        
    return render(request,'post/login.html')

'''
def suplogin(request):
    flag=2
    context={'flag':flag}
    if request.method == 'POST': 
        
        username = request.POST.get('user')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        
        if user is not None:
            auth_login(request, user)
        # Redirect to a success page.
            return redirect('iqac') 
        
        else: 
            flag=0 
            context = {'flag':flag}
            return render(request,'post/login.html',context) 
        
    return render(request,'post/login.html')

'''


'''def post_d(request):
    username = request.POST.get('user')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('admin@post.html')        
   ''' 

def admin_post(request): 
    post = MkPost.objects.all() 
    if request.method == "POST":
        item = request.POST.get('search')
        post = Post.objects.filter(title__contains=item) 
        context = {'post':post}
        render(request,'post/admin@post.html',context) 

    context = {'posts':post}

    return render(request,'post/admin@post.html',context) 

def iqac(request): 
    post = MkPost.objects.all() 
    if request.method == "POST":
        item = request.POST.get('search')
        post = Post.objects.filter(title__contains=item) 
        context = {'post':post}
        render(request,'post/sup.html',context) 

    context = {'posts':post}

    return render(request,'post/sup.html',context) 
'''
def update(request,pk):
    post = Post.objects.get(id=pk)
'''

def delete(request,id):
    post = MkPost.objects.get(id=id)
    if post.img:
        image = post.img.url
    if os.path.isfile(image):
       os.remove(image)
    post.delete()
    return redirect('admin@post')

def ac(request,id):
    post = MkPost.objects.get(id=id)
    '''
    image = post.img.url
    if os.path.isfile(image):
       os.remove(image)
       '''
    post.delete()
    return redirect('active')


def detail(request,id):
    post = MkPost.objects.get(id=id)
    context = {'post':post}
    return render(request,'post/detail.html',context)

def reqdetail(request,id):
    post = MkPost.objects.get(id=id)
    context = {'post':post}
    return render(request,'post/detail.html',context)


def logout(request):
    auth_logout(request) 
    return redirect('home') 

def approve(request,id):
    post = MkPost.objects.get(id=id)
    post.approved = True
    
    
'''

def active(request):
    post = ApprovedPost.objects.all()
    if request.method == "POST":
        if request.POST != '':
            item = request.POST.get('search')
            post = ApprovedPost.objects.filter(title__contains=item) 
            context = {'post':post}
            return render(request,'post/activeposts.html',context)
        else:
             context = {"posts":post}
             return render(request,'post/activeposts.html',context)

    context = {'posts':post}
    return render(request,'post/activeposts.html',context)
'''