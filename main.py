from youtube_audio_downloader import Youtube_audio_downloader
from split import Spleeter


aDownloader = Youtube_audio_downloader("inputFile.txt")
aDownloader.run()

aSplitter = Spleeter()
print(aSplitter.mp4_list)
aSplitter.run()
