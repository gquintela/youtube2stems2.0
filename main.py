from downloader import Downloader
from split import Spleeter


aDownloader = Downloader("inputFile.txt")
aSplitter = Spleeter()

try:
    aDownloader.download_list_to_mp4()
except:
    print("Error while downloading the songs.")

try:
    aSplitter.split()
except:
    print("Error while splitting the songs.")
