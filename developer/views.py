from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import *
from .forms import *
import os
from django.conf import settings

# Create your views here.

@login_required(login_url="/accounts/signup")
def home_view(request):
    profiles_list=AllProfile.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(profiles_list, 3)
    try:
        profiles = paginator.page(page)

    except PageNotAnInteger:
        profiles = paginator.page(1)

    except EmptyPage:
        profiles = paginator.page(paginator.num_pages)

    return render(request,'developerProfiles.html',{ 'profiles':profiles})


def profile_view(request, pk):
    if request.method == "POST":
        sender=AllProfile.objects.get(user=request.user)
        reciever=AllProfile.objects.filter(id=pk)
        profile=reciever
        msg=Invitation()
        msg.inviter=sender
        for field in reciever.all():
            msg.invitee=field.user

        msg.save()
        return render(request, 'profileview.html', {'profile':profile})
    else:
        profile=AllProfile.objects.filter(id=pk)
        return render(request, 'profileview.html', {'profile':profile})

def invites_view(request):
    invites=Invitation.objects.filter(invitee=request.user)
    return render(request, 'invites.html', {'invites':invites})

def inviter_view(request, pk):
    profile=AllProfile.objects.filter(id=pk)
    return render(request, 'profileview.html', {'profile':profile})

def accept_response_view(request, pk, id):
    if request.method=="POST":
        Sender=AllProfile.objects.filter(id=pk)
        Accepter=AllProfile.objects.get(user=request.user)
        msg=Response()
        for field in Sender.all():
            msg.sender=field.user
        msg.accepter=Accepter
        msg.save()
        invites=Invitation.objects.filter(invitee=request.user)
        return render(request, 'invites.html', {'invites':invites})
    else:
        invites=Invitation.objects.filter(invitee=request.user)
        return render(request, 'invites.html', {'invites':invites})

def request_accepted_view(request):
    accepters=Response.objects.filter(sender=request.user).order_by('-id')
    return render(request, 'responses.html', {'accepters': accepters})


def filldetails_view(request):
    if request.method=="POST":
        profile=AllProfile()
        profile.name=request.POST['name']
        profile.email=request.POST['email']
        if request.POST['react']:
            profile.react=request.POST['react']
        if request.POST['angular']:
            profile.angular=request.POST['angular']
        elif request.POST['vuejs']:
            profile.vuejs=request.POST['vuejs']
        profile.user=request.user
        profile.profile_pic=request.FILES['profile_pic']
        if request.POST['bootstrap']:
            profile.bootstrap=request.POST['bootstrap']
        profile.Git_Hub_Url=request.POST['Git_Hub_Url']
        profile.LinkedIn_Url=request.POST['LinkedIn_Url']
        if request.POST['django']:
            profile.django=request.POST['django']
        if request.POST['flask']:
            profile.flask=request.POST['flask']
        if request.POST['php']:
            profile.php=request.POST['php']
        if request.POST['nodejs']:
            profile.nodejs=request.POST['nodejs']
        if request.POST['javascript']:
            profile.javascript=request.POST['javascript']
        if request.POST['css']:
            profile.css=request.POST['css']


        profile.save()
        return redirect('/')
    else:
        return render(request, 'filldetails.html')






def profile_edit_form( request ):
    profile=AllProfile.objects.filter(user=request.user)
    if request.method=="POST":
        profile=AllProfile.objects.filter(user=request.user).update(
            name=request.POST['name'],
            email=request.POST['email'],
            Git_Hub_Url=request.POST['Git_Hub_Url'],
            LinkedIn_Url=request.POST['LinkedIn_Url']
        )
        old_image=AllProfile.objects.get(user=request.user)
        form = ImageForm(request.POST, request.FILES, instance=old_image)
        if form.is_valid():
            image_path = old_image.profile_pic.path
            if os.path.exists(image_path):
                os.remove(image_path)
            form.save()
            profile=AllProfile.objects.filter(user=request.user)
            return render( request, 'myprofile.html',{'profile':profile})
    else:
        return render( request, 'profileEdit.html',{'profile':profile})
