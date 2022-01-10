from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from hoodapp.forms import BusinessForm, HoodForm, PostForm, ProfileForm,UpdateProfileForm
from .models import Profile,Neighborhood,Post,Business,Location


# Create your views here.

def index(request):
    return render(request, 'all-hood/index.html')


@login_required(login_url="/accounts/login/")
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    neighborhood = Neighborhood.objects.all()
    businesses = Business.objects.all().order_by('-id')
    posts = Post.objects.all().order_by('-id')
    return render(request, "profile.html", {"profile": profile, ' neighborhood':  neighborhood, 'businesses': businesses, 'posts' : posts})


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
    current_user = request.user
    hood = Neighborhood.objects.get(name=name)
    businesses = Business.objects.filter(neighborhood=hood)
    posts = Post.objects.filter(neighborhood=hood)
    
    
    return render(request,'lone_hood.html',{'hood':hood,"businesses": businesses ,"posts": posts})    

def neighborhoods(request):
    all_neighborhoods = Neighborhood.objects.all()
    all_neighborhoods = all_neighborhoods[::-1]
    return render(request, 'neighborhood.html',{'all_neighborhoods': all_neighborhoods})


def join_hood(request,id):
    neighborhood = get_object_or_404(Neighborhood, id=id)
    
    request.user.profile.neighborhood = neighborhood
    request.user.profile.save()
    return redirect('hood')

def leave_hood(request, id):
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

@login_required(login_url="/accounts/login/")
def create_business(request):
    current_user = request.user
    if request.method == "POST":
        
        form=BusinessForm(request.POST,request.FILES)

        if form.is_valid():
            business=form.save(commit=False)
            business.user=current_user
            business.hood= hood
            business.save()
        return HttpResponseRedirect('/businesses')
    else:
        form=BusinessForm()
    return render (request,'business_form.html', {'form': form, 'profile': profile})


@login_required(login_url="/accounts/login/")
def businesses(request):
    current_user = request.user
    businesses = Business.objects.all().order_by('-id')
    
    profile = Profile.objects.filter(user_id=current_user.id).first()

    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()
        
        locations = Location.objects.all()
        neighborhood = Neighborhood.objects.all()
        
        businesses = Business.objects.all().order_by('-id')
        
        return render(request, "profile.html", {"danger": "Update Profile", "locations": locations, "neighborhood": neighborhood, "businesses": businesses})
    else:
        neighborhood = profile.neighborhood
        businesses = Business.objects.all().order_by('-id')
        return render(request, "business.html", {"businesses": businesses})  

login_required(login_url="/accounts/login/")
def create_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user=current_user
            post.save()
            return redirect('/posts')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})

def posts(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    posts = Post.objects.filter(user_id=current_user.id)
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first() 
        posts = Post.objects.filter(user_id=current_user.id)
        
        locations = Location.objects.all()
        neighborhood = Neighborhood.objects.all()
        
        businesses = Business.objects.filter(user_id=current_user.id)
        
        return render(request, "profile.html", {"danger": "Update Profile ", "locations": locations, "neighborhood": neighborhood,  "businesses": businesses,"posts": posts})
    else:
        neighborhood = profile.neighborhood
        posts = Post.objects.filter(user_id=current_user.id)
        return render(request, "posts.html", {"posts": posts}) 

@login_required(login_url="/accounts/login/")
def search(request):
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_hood = Neighborhood.objects.filter(name__icontains=search_term)
        message = f"Search For: {search_term}"

        return render(request, "search.html", {"message": message, "hood": searched_hood})
    else:
        message = "You haven't searched for any term"
        return render(request, "search.html", {"message": message})                

    
