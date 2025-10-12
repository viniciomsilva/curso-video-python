from csv import reader
from pathlib import Path
from pygame import mixer
from pygame import time


class MusicPlayer:

    def __init__(self):
        self.__song_filename: Path

        self.__playlist_path = (
            Path(__file__)
            .parent.parent.joinpath(
                "assets",
                "task021_songs",
            )
            .resolve()
        )
        self.__playlist = self.__load_playlist()
        mixer.init()

    @property
    def playlist(self) -> list[dict]:
        return self.__playlist

    def __read_map_file(self) -> list:
        with open(
            Path.joinpath(
                self.__playlist_path,
                ".map.csv",
            ).resolve()
        ) as file:
            return list(reader(file))

    def __load_playlist(self) -> list[dict]:
        return [
            {
                "title": data[0],
                "artist": data[1],
                "filename": data[2],
            }
            for data in self.__read_map_file()
        ]

    def select(self, option: int) -> dict:
        if (option <= 0) or (option > len(self.__playlist)):
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

    def quit(self) -> None:
        mixer.quit()
