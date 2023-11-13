from pytube import YouTube
from sys import argv
link=input("Enter Youtube video link to download\n")
try:
    yt=YouTube(link)
    a=input("Resolution of the video?(High/Low) or if you need to download only audio(Type Audio)\n")
    if a=="High":
        video = yt.streams.get_highest_resolution()
    elif a=="Low":
        video = yt.streams.get_lowest_resolution()
    elif a=="Audio":
        video=yt.streams.get_audio_only()
    else:
        print("Enter High/Low/Audio\n")
    video.download()
    print("Video Successfully downloaded")
except:
    print("Error in your input")