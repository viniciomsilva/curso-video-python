from pathlib import Path
from pygame import mixer
from pygame import time

from scripts import database as db


class MusicPlayer:

    def __init__(self):
        self.__song_filename: Path

        self.__playlist_path: Path = (
            Path(__file__)
            .parent.parent.joinpath(
                "data",
                "playlist_songs",
            )
            .resolve()
        )
        self.__playlist: list = self.__load_playlist()
        mixer.init()

    @staticmethod
    def quit() -> None:
        mixer.quit()

    @property
    def playlist(self) -> list:
        return self.__playlist

    def __load_playlist(self) -> list:
        return [
            {
                "title": data[0],
                "artist": data[1],
                "filename": data[2],
            }
            for data in db.read_csv("playlist.csv")
        ]

    def select(self, option: int) -> dict:
        if option <= 0 or option > len(self.__playlist):
            raise Exception("Music does not exists.")

        option -= 1
        self.__song_filename = Path.joinpath(
            self.__playlist_path,
            self.__playlist[option]["filename"],
        ).resolve()

        return self.__playlist[option]

    def play(self, milliseconds: int = 60000) -> None:
        mixer.music.load(self.__song_filename)
        mixer.music.play()
        time.wait(milliseconds)
        mixer.music.stop()
