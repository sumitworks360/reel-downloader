from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
import yt_dlp
import os
from django.http import FileResponse
from dotenv import load_dotenv
import requests

load_dotenv()


def home(request):
    return render(request, 'index.html')


@api_view(['POST'])
def download_reel(request):
    url = request.data.get('url')

    if not url:
        return Response({"error": "URL is required"}, status=400)

    try:
        api_url = "https://instagram-reels-downloader-api.p.rapidapi.com/download"

        headers = {
            "x-rapidapi-key": "38b56b4befmsh1a6dff3dbf209ecp125cb2jsn7a7369085ef3",
            "x-rapidapi-host": "instagram-reels-downloader-api.p.rapidapi.com"
        }

        params = {
            "url": url
        }

        response = requests.get(api_url, headers=headers, params=params)
        data = response.json()

        # 🔥 IMPORTANT: Extract correct video URL
        video_url = data.get("data", {}).get("download_url")

        if not video_url:
            return Response({"error": "Failed to fetch video"}, status=400)

        return Response({
            "download_url": video_url
        })

    except Exception as e:
        return Response({"error": str(e)}, status=500)

