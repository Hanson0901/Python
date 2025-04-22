from ytmusicapi import YTMusic
import yt_dlp

# 使用者輸入
song_name = input("請輸入歌曲名稱：")
artist = input("請輸入歌手名稱：")
search_query = f"{artist} {song_name}"

# 用 ytmusicapi 搜尋
ytmusic = YTMusic()
results = ytmusic.search(search_query, filter="songs")
if not results:
    print("找不到歌曲")
    exit()

videoId = results[0]['videoId']
url = f"https://music.youtube.com/watch?v={videoId}"

# yt-dlp 下載 FLAC 並嵌入封面
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{artist} - {song_name}.%(ext)s',
    'postprocessors': [
        {
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
        },
        {
            'key': 'EmbedThumbnail',
        },
        {
            'key': 'FFmpegMetadata',
        }
    ],
    'writethumbnail': True,
    'embedthumbnail': True,
    'addmetadata': True,
    'quiet': True,
    'no_warnings': True,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print(f"下載完成：{artist} - {song_name}.flac")
