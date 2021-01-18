from pytube import YouTube

url = str(input("Enter /  Paste The Link : \n"))

yt = YouTube(url)

stream = yt.streams.first()

stream.download()

print("Please Wait ... | Dont close the terminal . It Will Automatically Close When Video Is Downloaded...  :)")