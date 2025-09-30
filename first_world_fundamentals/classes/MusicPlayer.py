from csv import reader
from os.path import join
from pygame import mixer, time

from classes import Song

class MusicPlayer:

    def __init__(self):
        self.MAP_FILENAME: str = "_map.csv"
        self.__song_filename: str = ""
        self.__playlist_path: str = ""
        self.__playlist: list[Song] = []

    @staticmethod
    def init() -> None:
        mixer.init()

    @staticmethod
    def quit() -> None:
        mixer.quit()

    def print_playlist(self) -> None:
        print("\nMÚSICAS DISPONÍVEIS\n")
        for i, song in enumerate(self.__playlist):
            print(f"#{(i + 1)} {song.title} - {song.artist}")
        print()

    def load(self, playlist_path) -> None:
        self.__playlist_path = playlist_path

        with open(join(
            self.__playlist_path, self.MAP_FILENAME
        ), "r") as map_file:
            csv_data = reader(map_file)
            for data in csv_data:
                self.__playlist.append(Song(data[0], data[1], data[2]))

    def select(self, i: int) -> Song:
        i -= 1
        self.__song_filename = join(
            self.__playlist_path, self.__playlist[i].filename
        )
        return self.__playlist[i]

    def play(self, d: int) -> None:
        mixer.music.load(self.__song_filename)
        mixer.music.play()
        time.wait((d * 1000))
        mixer.music.stop()
