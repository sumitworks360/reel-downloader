from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework.response import Response
import yt_dlp
import os
from django.http import FileResponse
from dotenv import load_dotenv

load_dotenv()


def home(request):
    return render(request, 'index.html')


@api_view(['POST'])
def download_reel(request):
    url = request.data.get('url')

    if not url:
        return Response({"error": "URL is required"}, status=400)

    try:
        output_path = "downloads"
        os.makedirs(output_path, exist_ok=True)

        ydl_opts = {
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
            'format': 'mp4'
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)

        return FileResponse(open(filename, 'rb'), as_attachment=True)

    except Exception as e:
        return Response({"error": str(e)}, status=500)
    

