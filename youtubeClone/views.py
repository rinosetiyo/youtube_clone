from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from channel.models import Channel
from youtubeClone.models import Video, Comment
from youtubeClone.forms import CommentForm

# Create your views here.
def index(request):
    videos = Video.objects.all()
    context = {
        "videos": videos,
    }
    return render(request, "index.html", context)

def video_detail(request, video_id):
    video = get_object_or_404(Video, id=video_id)
    comments = Comment.objects.filter(video=video)

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid:
            # parent_obj = None
            # if request.POST.get("parent_id"):
            #     parent = request.POST.get("parent_id")
            #     parent_obj = Comment.objects.get(id=parent)
            comment = comment_form.save(commit=False)
            get_video_id = request.POST.get("video_id")
            video = Video.objects.get(id=get_video_id)
            comment.video = video
            comment.user = request.user
            comment.save()
    else:
        comment_form = CommentForm()

    context = {
        "video": video,
        "comment_form": comment_form,
        "comments": comments,
    }
    return render(request, "video.html", context)

def channel_view(request, channel_id):
    channel = Channel.objects.get(id=channel_id)
    videos = Video.objects.filter(channel=channel)
    context = {
        "channel": channel,
        "videos": videos,
    }
    return render(request, "channel.html", context)


# def add_new_subscribers(request, channel_id):
#     subs = Channel.objects.get(id=channel_id)
#     user = request.user

#     if user in subs.subscribers.all():
#         subs.subscribers.remove(user)
#         response = "Unsubscribed"
#         return JsonResponse(response, safe=False, staus=200)
#     else:
#         subs.subscribers.add(user)
#         response = "Subscribed"

# def load_subscribers(request, channel_id):
#     subs = Channel.objects.get(id=channel_id)
#     subs_lists = list(subs.subscribers.values())
#     return JsonResponse(subs_lists, safe=False, status=200)

# def like_video(request, video_id):
#     video = Video.objects.get(id=video_id)
#     user = request.user

#     if user in video.likes.all():
#         video.likes.remove(user)
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
#         # response = "Disliked"
#         # return JsonResponse(response, safe=False, status=200)
#     else:
#         video.likes.add(user)
#         return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
#         # response = "Liked"
#         # return JsonResponse(response, safe=False, status=200)

# def load_likes(request, video_id):
#     video = Video.objects.get(id=video_id)
#     likes = list(video.likes.values())
#     return JsonResponse(likes, safe=False, status=200)

# def save_video(request, video_id):
    video = Video.objects.get(id=video_id)
    user = request.user.profile

    if user in video.saved_videos.all():
        video.saved_videos.remove(user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        video.saved_videos.add(user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))