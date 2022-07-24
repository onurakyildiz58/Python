from moviepy.editor import VideoFileClip
from pytube import YouTube
import os, shutil

link = str(input("linki giriniz : "))
print("indiriliyor.....")
mp4 = YouTube(link).streams.get_highest_resolution().download()
mp3 = mp4.split(".mp4", 1)[0] + ".mp3"
video_kes = VideoFileClip(mp4)
ses_kes = video_kes.audio
ses_kes.write_audiofile(mp3)
ses_kes.close()
video_kes.close()
os.remove(mp4)
shutil.move(mp3, r"C:\\Users\\onura\\Desktop\\Ferhat Akyıldız\\music")
