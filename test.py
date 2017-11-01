from devices.lighting.hue import hue
import requests
import json
import utils

h = hue.Hue()

# print("Light groups", h.getAllGroups())
# print()
# print("Get all Lights", h.getAllLights())
# print()
l = h.getLightDetails('1')
print(l[1]['name'])

# print("PUT", h._getPutUrl('2'))
# print(h.turnDeviceOff('2'))
# print(h.toggle('2'))

json_object = json.loads('{"foo":"bar"}')
utils.print_json_str('{"foo":"bar"}')
utils.print_json_obj(json_object)