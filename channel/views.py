from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

# @login_required
# def add_comment(request, video_id):
#    video = Video.objects.get(id=video_id)
#    user = request.user
#    comment = request.POST.get('comment')
#    Comment.objects.create(video=video, user=user, comment=comment)
#    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))