# modules: import, from, as, dir, help, reload

import dog

print(dog.bark())

from dog import bark
print(bark())

import lib.cat
print(lib.cat.talk())

from lib.cat import talk
print(talk())
