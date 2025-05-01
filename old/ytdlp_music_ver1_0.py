from ytmusicapi import YTMusic
import yt_dlp
from mutagen.flac import FLAC, Picture
import re
import requests
import os
# 確保檔案名稱不包含非法字元
def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', '_', name).strip()

# 使用者輸入
song_name = input("請輸入歌曲名稱：")
artist = input("請輸入歌手名稱：")

# 清理非法字元
safe_song = sanitize_filename(song_name)
safe_artist = sanitize_filename(artist)
output_file = f"{safe_artist} - {safe_song}.flac"

# 用 ytmusicapi 搜尋並取得資料
ytmusic = YTMusic()
results = ytmusic.search(f"{artist} {song_name}", filter="songs")
if not results:
    print("找不到歌曲")
    exit()

info = results[0]
video_id = info['videoId']
thumbnail_url = info['thumbnails'][-1]['url']

# 提取專輯名稱 (最新版 ytmusicapi 0.19.2+ 支援)
album_name = info.get('album', {}).get('name', '') if 'album' in info else ''

# 下載 FLAC
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': output_file.replace('.flac', '.%(ext)s'),
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'flac',
    }],
    'writethumbnail': True,
    'quiet': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([f"https://music.youtube.com/watch?v={video_id}"])

# 嵌入元數據與封面
if os.path.exists(output_file):
    audio = FLAC(output_file)
    audio["title"] = song_name
    audio["artist"] = artist
    
    # 寫入專輯名稱（如果存在）
    if album_name:
        audio["album"] = album_name
    
    # 下載並嵌入封面
    img_data = requests.get(thumbnail_url).content
    image = Picture()
    image.data = img_data
    image.type = 3  # 封面類型
    image.mime = "image/jpeg" if thumbnail_url.endswith("jpg") else "image/png"
    audio.add_picture(image)
    audio.save()
    print(f"成功保存：{output_file}")
else:
    print("錯誤：FLAC 檔案未生成")
# 最終檢查：手動清理可能的殘留檔案
for f in os.listdir():
    if f.endswith(".webp"):
        os.remove(f)