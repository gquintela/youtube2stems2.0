from pytube import YouTube


class Downloader:
    def __init__(self, input_file):
        self.input_file_name = input_file
        self.url_list = []

    def parse_list(self):
        input_file = open(self.input_file_name, "r")
        while True:
            link = input_file.readline()  # Get next link from file
            if not link:  # if line is empty or end of file is reached
                break
            self.url_list.append(link)
        input_file.close()

    def download_list_to_mp4(self):
        self.parse_list()
        for link in self.url_list:
            yt = YouTube(link)
            print(f"Downloading: {yt.title}...")
            stream = yt.streams.filter(only_audio=True, audio_codec="mp4a.40.2")
            stream.last().download()
