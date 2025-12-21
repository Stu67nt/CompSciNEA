import yt_dlp

def download(urls: list, config: dict):
    with yt_dlp.YoutubeDL(config) as ydl:
        ydl.download(urls)

config = {
    "verbose": True,
    "format": "",
    "paths": "",
    "outtmpl": "",
    "windowsfilenames": True,
    "ignoreerrors": False,
    "playlist_items": "",
    "lazy_playlist": "",
    "matchtitle": "",
    "logger": "",
    "logtostderr": "",
    "writethumbnail": "",
    "download_archive": "",
    "cookiefile": "",
    "cookiesfrombrowser": "",
    "postprocessors": "",
    "progress_hooks": "",
    "postprocessor_hooks": "",
    "progress_template": "",
    "playliststart": "",
    "playlistend": "",
    "playlistreverse": ""
}

help(yt_dlp.YoutubeDL)