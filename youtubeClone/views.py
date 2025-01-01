from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from channel.models import Channel
from youtubeClone.models import Video

# Create your views here.
def index(request):
    videos = Video.objects.all()
    context = {
        "videos": videos,
    }
    return render(request, "index.html", context)

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