# 021
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM ÁUDIO DE UM ARQUIVO MP3

from csv import reader
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
        self.MAP_FILENAME: str = '_map.csv'
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
        for i, song in enumerate(self.__playlist):
            print(f'#{(i + 1)} {song.title} - {song.artist}')
        print()

    def load(self, playlist_path: str) -> None | Exception:
        """
        Loads the initial information, the playlist parent's directory, and the playlist itself from the '_map.csv'
        file so the player can work.

        :param playlist_path: Song list parent directory
        :return None or an error message if the file is not found
        """
        self.__playlist_path = playlist_path
        try:
            with open(path.join(self.__playlist_path, self.MAP_FILENAME), 'r') as map_file:
                csv_data = reader(map_file)
                for data in csv_data:
                    self.__playlist.append(Song(data[0], data[1], data[2]))
        except:
            raise Exception(f'\nARQUIVO "{path.join(self.__playlist_path, self.MAP_FILENAME)}" NÃO ENCONTRADO!!!')

    def select(self, i: int) -> Song | Exception:
        """
        Selects a song from the catalog.

        :param i: Index: Option desired by the user
        :return: The selected song or an error message if there is no valid option in the song catalog
        """
        if i <= 0 or i > len(self.__playlist):
            raise Exception('\nPOR FAVOR, SELECIONE UMA MÚSICA PRESENTE NO CATÁLOGO!')
        else:
            i -= 1
            self.__song_filename = path.join(self.__playlist_path, self.__playlist[i].filename)
            return self.__playlist[i]

    def play(self, d: int) -> None | Exception:
        """
        Plays the chosen song from the catalog for a certain period of time.

        :param d: Player duration, in seconds
        :return None or an error message if the file is not found
        """
        try:
            mixer.music.load(self.__song_filename)
            mixer.music.play()
            time.wait((d * 1000))
            mixer.music.stop()
        except Exception:
            raise Exception(f'\nARQUIVO "{self.__song_filename}" NÃO ENCONTRADO!!!')


if __name__ == '__main__':
    try:
        player = MusicPlayer()

        player.init()
        player.load(path.join(path.dirname(getcwd()), 'media', 'task021_songs'))
        player.print_playlist()

        while True:
            try:
                option = int(input('SELECIONE UMA MÚSICA................................: #'))
                selected = player.select(option)

                print(f'ESTÁ TOCANDO AGORA..................................: {selected.title} - {selected.artist}')
                player.play(60)  # default duration: 60 seconds

                if input('QUER OUVIR OUTRA? [y/n].............................: ') != 'y':
                    player.quit()
                    break

                print()
            except Exception as e:
                print(e)
    except Exception as e:
        print(e)
