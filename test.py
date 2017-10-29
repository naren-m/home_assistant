from devices.lighting.hue import hue
import requests
import json

h = hue.Hue()

print("Light groups", h.getAllGroups())
print()
print("Get all Lights", h.getAllLights())
print()
print(h.getLightDetails('1'))

print("PUT", h._getPutUrl('2'))
# print(h.turnDeviceOff('2'))
print(h.toggle('2'))
