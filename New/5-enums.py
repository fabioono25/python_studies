# working with enums
from enum import Enum


class State(Enum):
    START = 0
    PLAYING = 1
    END = 2
    OTHER = '123123'

print(State.START)
print(State.PLAYING.value)
print(State['END'].value)
print(State.OTHER.value)
print(len(State))