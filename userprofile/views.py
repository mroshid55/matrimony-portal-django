from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Profile,Notification,ChatMessage,Friend
from advertisement.models import Advertisement

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Chat
from .forms import ChatMessageForm
from django.http import JsonResponse
import json

# Create your views here.


@login_required(login_url='login')
def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        # Count followers and following
        followers_count = profile.followers.count()
        following_count = profile.following.count()
        # Profile view count
        profile.view_count = profile.view_count+1
        profile.save()
        # Advertisement show all profile
        ads = Advertisement.objects.filter(user_id=pk).order_by("-created_at")
        # Who profile view
        # who_user = User.objects.get(id=request.user.profile)
        # Whoprofileview.objects.create(user=who_user)
        # Post Form logic
        if request.method == "POST":
            # Get current user
            current_user_profile = request.user.profile
            # Notification for profile user
            user = User.objects.get(id=profile.id)
            # Get form data
            action = request.POST['follow']
            # Decide to follow or unfollow
            if action == "unfollow":
                current_user_profile.following.remove(profile)
                # Message for notification
                message = f'{current_user_profile.user.username} has sent you a unfollow request'
                Notification.objects.create(user=user, message=message)
            elif action == "follow":
                current_user_profile.following.add(profile)
                # Message for notification
                message = f'{current_user_profile.user.username} has sent you a follow request'
                Notification.objects.create(user=user, message=message)
                
            # Save the profile
            current_user_profile.save()

        return render(request, "profile/profile.html", {"profile": profile, "followers_count": followers_count, "following_count": following_count,"ads":ads})
    else:
        return redirect('login')


@login_required(login_url='login')
def all_people(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        context = {"profiles": profiles}
        return render(request, "profile/all-people.html", context)
    else:
        return redirect('login')


@login_required(login_url='login')
def followers(request, pk):
    if request.user.is_authenticated:
        profiles = Profile.objects.get(user_id=pk)
        context = {"profiles": profiles}
        return render(request, "profile/followers.html", context)
    else:
        return redirect('login')


@login_required(login_url='login')
def following(request, pk):
    if request.user.is_authenticated:
        profiles = Profile.objects.get(user_id=pk)
        context = {"profiles": profiles}
        return render(request, "profile/following.html", context)
    else:
        return redirect('login')



def updateprofile(request):
    context={}
    return render(request,"profile/profile-update.html",context)

####################################################### Notification ######################################################

def allnotifications(request):
    if request.user.is_authenticated:
        notifications= Notification.objects.filter(user=request.user).order_by("-timestamp")
    context={"notifications":notifications}
    return render(request,"notifications/all-notifications.html",context)


def deletenotifications(request,pk):
    if request.user.is_authenticated:
        delete_notifications= get_object_or_404(Notification,id=pk)
        delete_notifications.delete()
        return redirect('all-notifications')
    context={"delete_notifications":delete_notifications} 
    return render(request,"notifications/all-notifications.html",context)

####################################################### Chat ######################################################

def detail(request,pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id=friend.profile.id)
    chats = ChatMessage.objects.all()
    rec_chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user, seen=False)
    rec_chats.update(seen=True)
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect("detail", pk=friend.profile.id)
    context = {"friend": friend, "form": form, "user":user, 
               "profile":profile, "chats": chats, "num": rec_chats.count()}
    return render(request, "chat/message.html", context)

def sentMessages(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    data = json.loads(request.body)
    new_chat = data["msg"]
    new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=user, msg_receiver=profile, seen=False )
    print(new_chat)
    return JsonResponse(new_chat_message.body, safe=False)

def receivedMessages(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    arr = []
    chats = ChatMessage.objects.filter(msg_sender=profile, msg_receiver=user)
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse(arr, safe=False)
