from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import RegisterForm,AdvertisementForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from userprofile.models import Profile,Notification
from advertisement.models import Advertisement

# Create your views here.
@login_required(login_url='login')
def home(request):
	if request.user.is_authenticated:
		form = AdvertisementForm(request.POST or None)
		if request.method == "POST":
			if form.is_valid():
				ads_post = form.save(commit=False)
				ads_post.user = request.user
				ads_post.save()
				messages.success(request, ("Your Meep Has Been Posted!"))
				return redirect('home')
		profile = Profile.objects.filter(user=request.user)
		advertisements = Advertisement.objects.all().order_by("-created_at")
		followers_count = request.user.profile.followers.count()
		following_count = request.user.profile.following.count()
		unread_notifications = Notification.objects.filter(user=request.user, is_read=False).count()
		notifications= Notification.objects.filter(user=request.user).order_by("-timestamp")[0:10]
		user = request.user.profile
		friends = user.friends.all()
		context = {"user": user, "friends": friends,"form":form,"profile":profile,"followers_count":followers_count,"following_count":following_count,"advertisements":advertisements,"unread_notifications":unread_notifications,"notifications":notifications}
		return render(request, "home/home.html",context)
	else:
		return redirect('login')

def advertisement_like(request, pk):
	if request.user.is_authenticated:
		ads = get_object_or_404(Advertisement, id=pk)
		if ads.likes.filter(id=request.user.id):
			ads.likes.remove(request.user)
		else:
			ads.likes.add(request.user)
		
		return redirect(request.META.get("HTTP_REFERER"))
	else:
		messages.success(request, ("You Must Be Logged In To View That Page..."))
		return redirect('login')


def register_user(request):
	form = RegisterForm()
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			# email = form.cleaned_data['email']
			# Log in user
			user = authenticate(username=username, password=password)
			login(request,user)
			messages.success(request, ("You have successfully registered! Welcome!"))
			return redirect('home')
	context = {'form':form}
	return render(request, "login/register.html",context)


def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.success(request, ("There was an error logging in. Please Try Again..."))
			return redirect('login')

	else:
		return render(request, "login/login.html", {})
	
def logout_user(request):
	logout(request)
	messages.success(request, ("You Have Been Logged Out. Sorry to Meep You Go..."))
	return redirect('login')

