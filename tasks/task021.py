# 021
# FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM ÁUDIO DE UM ARQUIVO MP3


from os import getcwd, path
from pygame import mixer, time


class Music:
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


    def __init__(self):
        """
        Creates a simple music play with a sequencie of songs of your choice.
        """
        self.__song_filename: str = ''
        self.__song_list_path: str = ''
        self.__song_list: list[Music] = []


    def print_music_catalog(self):
        """
        Prints the songs in a numbered catalog.

        :return: None
        """
        print('\nCATÁLOGO DE MÚSICAS DISPONÍVEIS---------------------\n')
        for music in self.__song_list:
            print('#{} {} - {}'.format((self.__song_list.index(music) + 1), music.title, music.artist))
        print()


    def select_music(self, i: int):
        """
        Selects a song from the catalog.

        :param i: Index: Option desired by the user
        :return: Title of the selected song or error if there is no valid option in the song catalog
        """
        if i <= 0 or i > len(self.__song_list):
            raise Exception('POR FAVOR, SELECIONE UMA MÚSICA PRESENTE NO CATÁLOGO!')
        else:
            i -= 1
            self.__song_filename = path.join(self.__song_list_path, self.__song_list[i].filename)
            return self.__song_list[i]


    def load(self, song_list_path: str, song_list: list[Music]):
        """
        Loads the initial information, the playlist's parent directory, and the playlist itself, so the player can work.

        :param song_list_path: Song list parent directory
        :param song_list: Song list
        :return: None
        """
        self.__song_list_path = song_list_path
        self.__song_list = song_list

    def play(self, d: int):
        """
        Plays the chosen song from the catalog for a certain period of time.

        :param d: Player duration, in seconds
        :return: None
        """
        mixer.init()
        mixer.music.load(self.__song_filename)
        mixer.music.play()
        time.wait((d * 1000))
        mixer.music.stop()
        mixer.quit()


if __name__ == '__main__':
    try:
        player = MusicPlayer()
        player.load(
            path.join(path.dirname(getcwd()), 'media', 'task021_songs'), [
            Music('KILLING IN THE NAME', 'RAGE AGAINST THE MACHINE', 'killing-in-the-name.mp3'),
            Music('NINE LIVES', 'AEROSMITH', 'nine-lives.mp3'),
            Music('PARANOID', 'BLACK SABBATH', 'paranoid.mp3'),
            Music('WE WILL ROCK YOU', 'QUEEN', 'we-will-rock-you.mp3'),
            Music('YOU SHOOK ME ALL NIGHT LONG', 'AC/CD', 'you-shook-me-all-night-long.mp3')
        ])

        player.print_music_catalog()
        option = int(input('SELECIONE UMA MÚSICA................................: #'))

        select_music = player.select_music(option)

        # duration = int(input('POR QUANTO TEMPO VOCÊ QUER QUE TOQUE (S)............:  '))
        print('ESTÁ TOCANDO AGORA..................................: {} - {}'
              .format(select_music.title, select_music.artist))

        # player.play_music(duration)
        player.play(10)
    except Exception as e:
        print(e)
