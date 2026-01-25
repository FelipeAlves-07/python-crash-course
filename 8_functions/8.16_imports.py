import album_functions
from album_functions import make_album
from album_functions import make_album as ma
import album_functions as af
from album_functions import *

new_album = album_functions.make_album('linkin park', 'meteora')
print(new_album)

new_album = make_album('dragonforce', 'inhuman rampage')
print(new_album)

new_album = ma('avenged sevenfold', 'nightmare', 11)
print(new_album)

new_album = af.make_album('linkin park', 'hybrid theory')
print(new_album)

new_album = make_album('escape the fate', 'this war is ours')
print(new_album)