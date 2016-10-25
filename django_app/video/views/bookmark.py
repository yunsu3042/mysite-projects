__all__=['bookmark_add','bookmark_list','bookmark_detail']

from django.shortcuts import render,HttpResponse, redirect,get_object_or_404
from video.models import Video



def bookmark_add(request):
    try:
        kind = request.POST['kind']
        vidoeId = request.POST['videoId']
        title = request.POST['title']
        description = request.POST['description']
        publishedAt = request.POST['publishedAt']
        thumbnail_url = request.POST['thumbnail_url']
        path = request.POST['path']
        video = Video.objects.create(
            kind=kind,
            youtube_id=vidoeId,
            title=title,
            description=description,
            published_date=publishedAt,
            thumbnail_url=thumbnail_url,
        )
        msg = "{title} 영상을 북마크에 등록했습니다".format( title=video.title)
    except Exception as e:
        return HttpResponse("Exception! {error}".format(error=e.args))
    if path:
        return redirect(path)
    else:
        return redirect('video:bookmark_list')



def bookmark_list(request):
    videos = Video.objects.all()
    context = {
        'videos': videos
    }
    return render(request, 'video/bookmark_list.html', context)


def bookmark_detail(request,pk):
    video = Video.objects.get(pk=pk)
    context = {
        'video':video
    }
    return render(request, 'video/bookmark_detail.html', context)