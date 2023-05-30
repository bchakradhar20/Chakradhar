import urllib.request, urllib.parse, urllib.error 
import requests
import sys, os
file=os.path.dirname(sys.argv[0])
from pytube import YouTube
from pytube import Playlist
def videodown(link):
    youtube1=YouTube(link)
    print("Title of video is "+youtube1.title)
    video = youtube1.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first() 
    '''video = youtube1.streams.first()'''
    '''video=youtube1.streams.all()'''
    '''all formats'''
    '''vid=list(enumerate(video))
    for i in vid:
        print(i)
    strm=int(input("Select:"))'''
    video.download()
    print("DONE")
def onlyaudio(link):
    youtube1=YouTube(link)
    print("Title of video is "+youtube1.title)
    
    video=youtube1.streams.filter(only_audio=True).order_by('abr').desc().first()
    '''audio formats'''
    '''vid=list(enumerate(video))
    for i in vid:
        print(i)
    strm=int(input("Select:"))'''
    video.download()
    print("DONE")
def playlistdown(link):
    p=Playlist(link)
    print(f'Downloading : {p.title}')
    for j in p.videos:
        j.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()
    print("DONE")

print("Welcome")
while (True):
    print("1. Video download")
    print("2. Audio download")
    print("3. Playlist download")
    link=input("Enter link: ")
    r=requests.get(link,allow_redirects= False)
    def try_site(url):
        request = requests.get(url, allow_redirects=False)
        return request.status_code == 200
    print(try_site(link))
    print ("status code ",r.status_code)
    if r.status_code!=200:
        print("Invalid YouTube link")
        print("You are above to exit the program")
        exit()
    try:
        youtube1=YouTube(link)
        video = youtube1.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
    except Exception as e:
        print(e)
        print("Invalid input")
        print("You are above to exit the program")
        exit()
    n=int(input("Choose above"))
    
    match (n):
        case 1:
            videodown(link)
            break
        case 2:
            onlyaudio(link)
            break
        case 3:
            playlistdown(link)
            break
        case _:
            print("Invalid input")
            print("You are above to exit the program")
            exit()

print("File location is: ",file)
