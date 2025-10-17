# module source

from os import path
from sys import path as sys

# add a directory above in the system path
sys.append(path.join(path.dirname(__file__), ".."))

from classes.music_player import MusicPlayer
from classes.separate_number import SeparateNumber
from scripts import custom
from scripts import db
from scripts import terminal
