# module classes

from os import path
from sys import path as sys

# add a directory above in the system path
sys.append(path.join(path.dirname(__file__), ".."))
