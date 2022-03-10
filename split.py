import os
import subprocess
from datetime import date


class Spleeter:
    def __init__(self, mp4_input_list=[]):
        self.mp4_list = mp4_input_list
        self.stems_qty = 5
        self.folder_name = date.today().strftime("%Y-%m-%d") + "_separated_stems"
        self.execute_command_base = (
            "spleeter separate -c mp3 -o "
            + self.folder_name
            + f" -p spleeter:{self.stems_qty}stems"
        )

    def mp4_finder(self):
        dir = "./"  # search in current directory
        entries = os.listdir(dir)
        for file in entries:
            newFile = self.song_renamer(file)
            if ".mp" in newFile:  # .mp3, mp4 etc
                self.mp4_list.append(newFile)

    def song_renamer(self, song):
        new_name = song.replace("(", "[").replace(")", "]")  # .replace(" ","")
        os.rename(song, new_name)
        return new_name

    def split(self):
        self.mp4_finder()
        for song in self.mp4_list:
            print(f"\nSeparating: {song}")
            subprocess.call(self.execute_command_base + ' "' + song + '"', shell=True)
            os.remove(song)
