
from phue import Bridge
b = Bridge('10.0.1.29')

b.connect()
b.set_group(1, 'on', True)
