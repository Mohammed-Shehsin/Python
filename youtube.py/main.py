from pytube import YouTube
# from sys import argv

link=input("Enter the link : ")
yt=YouTube(link)

print("Title :",yt.title)
print("Views :",yt.views)
print("Author :",yt.author)
path=input("Enter where to download :")
yd=yt.streams.get_highest_resolution()
yd.download(path)
