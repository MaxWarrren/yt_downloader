from pytubefix import YouTube
import os

#update these to your own directory
audio_path = os.path.join(os.getcwd(), "converted/audio")
video_path = os.path.join(os.getcwd(), "converted/videos")

def download_yt(url, exportType):
    try:
        yt = YouTube(url)
        print("Title:", yt.title)

        if exportType == "mp3":
            print("Downloading audio as mp3")
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path=audio_path)
            print("Audio converted")
        elif exportType == "mp4":
            print("Downloading video as mp4")
            video_stream = yt.streams.get_highest_resolution()
            video_stream.download(output_path=video_path)
            print("Video converted!")
    
    except Exception as e:
        print(f"An error occurred: {e}")

#examples
#download_yt("https://www.youtube.com/watch?v=q9--XI4NhD8", "mp3")
#download_yt("https://www.youtube.com/watch?v=q9--XI4NhD8", "mp4")
