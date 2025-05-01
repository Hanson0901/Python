import yt_dlp as yt

# Example of extracting information or downloading a video
url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'

# Set up download options
ydl_opts = {
    'format': 'best'
}

# Using yt-dlp to download the video
with yt.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])