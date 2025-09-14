# 021
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM ÁUDIO DE UM ARQUIVO MP3

from os import getcwd, path

from pygame import mixer, time


class Song:
    """
    Class with information about a song: title; artist name; and MP3 file name.
    """

    def __init__(self, title: str, artist: str, filename: str):
        """
        Creates a song with title, artist name and file name.

        :param title: Music title
        :param artist: Artist name
        :param filename: MP3 file name
        """
        self.title = title
        self.artist = artist
        self.filename = filename


class MusicPlayer:
    """
    Class with methods for listing and playing songs.
    """

    def __init__(self):
        """
        Creates a simple music player with a sequence of songs of your choice.
        """
        self.__song_filename: str = ''
        self.__playlist_path: str = ''
        self.__playlist: list[Song] = []

    @staticmethod
    def init() -> None:
        """
        Start the mixer process.
        """
        mixer.init()

    @staticmethod
    def quit() -> None:
        """
        End the mixer process.
        """
        mixer.quit()

    def print_playlist(self) -> None:
        """
        Prints the songs in a numbered catalog.
        """
        print('\nMÚSICAS DISPONÍVEIS---------------------------------\n')
        for music in self.__playlist:
            print('#{} {} - {}'.format((self.__playlist.index(music) + 1), music.title, music.artist))
        print()

    def load(self, playlist_path: str, playlist: list[Song]) -> None:
        """
        Loads the initial information, the playlist's parent directory, and the playlist itself, so the player can work.

        :param playlist_path: Song list parent directory
        :param playlist: Song list
        """
        self.__playlist_path = playlist_path
        self.__playlist = playlist

    def select(self, i: int) -> Song | Exception:
        """
        Selects a song from the catalog.

        :param i: Index: Option desired by the user
        :return: The selected song or an error message if there is no valid option in the song catalog
        """
        if i <= 0 or i > len(self.__playlist):
            raise Exception('POR FAVOR, SELECIONE UMA MÚSICA PRESENTE NO CATÁLOGO!')
        else:
            i -= 1
            self.__song_filename = path.join(self.__playlist_path, self.__playlist[i].filename)
            return self.__playlist[i]

    def play(self, d: int) -> None:
        """
        Plays the chosen song from the catalog for a certain period of time.

        :param d: Player duration, in seconds
        """
        mixer.music.load(self.__song_filename)
        mixer.music.play()
        time.wait((d * 1000))
        mixer.music.stop()


if __name__ == '__main__':
    player = MusicPlayer()
    player.init()
    player.load(path.join(path.dirname(getcwd()), 'media', 'task021_songs'),
                [Song('KILLING IN THE NAME', 'RAGE AGAINST THE MACHINE', 'killing-in-the-name.mp3'),
                 Song('NINE LIVES', 'AEROSMITH', 'nine-lives.mp3'), Song('PARANOID', 'BLACK SABBATH', 'paranoid.mp3'),
                 Song('WE WILL ROCK YOU', 'QUEEN', 'we-will-rock-you.mp3'),
                 Song('YOU SHOOK ME ALL NIGHT LONG', 'AC/CD', 'you-shook-me-all-night-long.mp3')])
    player.print_playlist()

    while True:
        try:
            option = int(input('SELECIONE UMA MÚSICA................................: #'))
            selected_song = player.select(option)

            print('ESTÁ TOCANDO AGORA..................................: {} - {}'.format(selected_song.title,
                                                                                         selected_song.artist))
            player.play(60)

            if input('QUER OUVIR OUTRA? [y/n].............................: ') != 'y':
                player.quit()
                break

            print()
        except Exception as e:
            print(e)
