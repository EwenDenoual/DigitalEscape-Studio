from .classes import Room
from .enigme import Enigme1, Enigme2, Enigme3, Enigme4, Enigme5, Enigme6, Enigme7, Enigme8, Enigme11, Enigme12, Enigme13, Enigme14, Enigme15, Enigme16, Enigme21, Enigme22, Enigme23, Enigme24, Enigme25, Enigme26
from .enigme import Door1, Door2, Door3

Room1 = Room([Enigme1, Enigme2, Enigme3, Enigme4, Enigme5, Enigme6, Enigme7, Enigme8], Door1)
Room2 = Room([Enigme11, Enigme12, Enigme13, Enigme14, Enigme15, Enigme16], Door2)
Room3 = Room([Enigme21, Enigme22, Enigme23, Enigme24, Enigme25, Enigme26], Door3)

