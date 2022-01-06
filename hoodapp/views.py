from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from hoodapp.forms import BusinessForm, HoodForm, PostForm, ProfileForm,UpdateProfileForm
from .models import Profile,Neighborhood,Post,Business


# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request, 'all-hood/index.html')

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user = request.user
    title = "Create Profile"
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:
        form = ProfileForm()
    return render(request, 'create_profile.html', {"form": form, "title": title})

@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    neighborhood = Neighborhood.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    return render(request, "profile.html", {"profile": profile, ' neighborhood':  neighborhood, 'business': businesses})


@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    user = User.objects.get(id=id)
    profile = Profile.objects.get(user_id = user)
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
            form = UpdateProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():  
                
                profile = form.save(commit=False)
                profile.save()
                return redirect('profile') 
            
    return render(request, 'update_profile.html', {"form":form})

@login_required(login_url="/accounts/login/")
def create_hood(request):
    current_user = request.user
    if request.method == 'POST':
        hood_form = HoodForm(request.POST, request.FILES)
        if hood_form.is_valid():
            hood = hood_form.save(commit=False)
            hood.user = current_user
            hood.save()
        return HttpResponseRedirect('/hood')
    else:
        hood_form = HoodForm()
    context = {'hood_form':hood_form}
    return render(request, 'hood_form.html',context)

@login_required(login_url="/accounts/login/")
def hood(request):
    current_user = request.user
    hood = Neighborhood.objects.all().order_by('-id')
    return render(request, 'hoods.html', {'hood': hood})

@login_required(login_url='/accounts/login/')
def lone_hood(request,name):
    hood = Neighborhood.objects.get(name=name)
    
    return render(request,'lone_hood.html',{'hood':hood})    

def neighborhoods(request):
    all_neighborhoods = Neighborhood.objects.all()
    all_neighborhoods = all_neighborhoods[::-1]
    return render(request, 'neighborhood.html',{'all_neighborhoods': all_neighborhoods})


def join_neighborhood(request, id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('hood')


def leave_neighborhood(request, id):
    hood = get_object_or_404(Neighborhood, id=id)
    request.user.profile.neighborhood = None
    request.user.profile.save()
    return redirect('hood')    


def create_post(request, hood_id):
    hood = Neighborhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('lone_hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})    

    
