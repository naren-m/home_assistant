# Philips Hue development

## Develpement references
[Getting started](https://www.developers.meethue.com/documentation/getting-started)
[Get bridge ip](www.meethue.com/api/nupnp)

# TODO
- [ ] Move configurations to the config module

# Philips hue api endpoints
GET Requests
'''
Information of all lights     - http://<bridge ipaddress>/api/<Access Token>/lights
Information of specific light - http://<bridge ipaddress>/api/<Access Token>/lights/<light id>

'''
PUT Requests
'''
Control lights                - http://<bridge ip address>/api/<Access Token>/lights/1/state
{"on":true, "sat":254, "bri":254,"hue":10000}
'''

## Example
'''
[Get list of all lights](http://10.0.1.2/api/Ny3OWGNNhMTM5SOVKdiIuEOB-scDUGFXXllFFacF/lights)
[Get info for a specific light](http://10.0.1.2/api/Ny3OWGNNhMTM5SOVKdiIuEOB-scDUGFXXllFFacF/lights/1)
'''
