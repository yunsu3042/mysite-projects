from django.shortcuts import render
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from oauth2client.tools import argparser
from video.models import Video

__all__=['youtube_search']

DEVELOPER_KEY = "AIzaSyDiarbwPOxSkXmNPfdv8UtHcZM6KySpk34"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"


def youtube_search(keyword, page_token, max_results=10):
    """
    youtube_search함수 개선

    1. youtube_search 함수의 arguments에 pageToken 추가
    2. 받은 pageToken값을 youtube.search()실행 시 list의 인자로 추가
    3. search뷰에서 request.GET에 pageToken값을 받아오도록 설정
    4. template에서 이전페이지/다음페이지 a태그 href에 GET parameter가 추가되도록 설정
    """
    youtube = build(
        YOUTUBE_API_SERVICE_NAME,
        YOUTUBE_API_VERSION,
        developerKey=DEVELOPER_KEY
    )

    search_response = youtube.search().list(
        q=keyword,
        part="id,snippet",
        maxResults=max_results,
        pageToken=page_token,
        type='video',
    ).execute()

    video_id_list = []

    for item in search_response['items']:
        video_id_list.append(item['id']['videoId'])
    str_id_list = ",".join(video_id_list)

    video_response = youtube.videos().list(
        part="snippet,statistics",
        id=str_id_list,
    ).execute()
    #print("search_response : {search_response}".format(search_response=search_response))

    try:
        video_response['prevPageToken'] = search_response['prevPageToken']
    except:
        pass
    try:
        video_response['nextPageToken'] = search_response['nextPageToken']
    except:
        pass
    try:
        video_response['totalResults'] = search_response['pageInfo']['totalResults']
    except:
        pass

    #print("video_response : {video_response}".format(video_response=video_response))

    for item in video_response['items']:
        cur_video_id = item['id']

        if Video.objects.filter(youtube_id=cur_video_id):
            item['is_exist']=True
        else:
            item['is_exist']=False
        print("is_exist?{}".format(item['is_exist']))

    return video_response

