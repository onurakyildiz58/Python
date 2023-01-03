from pytube import YouTube

path = "videos"

with open('links.txt') as f:
    lines = f.readlines()
    links = str(lines)
    for i in lines:
        Video = YouTube(i)
        title = Video.title
        Video = Video.streams.get_highest_resolution()
        Video.download()
