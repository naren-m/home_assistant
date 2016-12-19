# Philips Hue development

## Develpement references
- [Getting started](https://www.developers.meethue.com/documentation/getting-started)
- [Get bridge ip](www.meethue.com/api/nupnp)

# TODO
- [ ] Move configurations to the config module

# [Philips hue core concepts](https://www.developers.meethue.com/documentation/core-concepts)

## Endpoints
- /lights resource which contains all the light resources
- /groups resource which contains all the groups
- /config resource which contains all the configuration items
- /schedules which contains all the schedules
- /scenes which contains all the scenes
- /sensors which contains all the sensors
- /rules which contains all the rules

# Philips hue api endpoints

GET Requests
```
Information of all lights     - http://{bridge ipaddress}/api/{Access Token}/lights

Information of specific light - http://{bridge ipaddress}/api/{Access Token}/lights/{light id}

```
PUT Requests
```
Control lights                - http://{bridge ip address}/api/{Access Token}/lights/1/state

Payload                       - {"on":true, "sat":254, "bri":254,"hue":10000}
```

## Example

- [Get list of all lights](http://10.0.1.2/api/Ny3OWGNNhMTM5SOVKdiIuEOB-scDUGFXXllFFacF/lights)
- [Get info for a specific light](http://10.0.1.2/api/Ny3OWGNNhMTM5SOVKdiIuEOB-scDUGFXXllFFacF/lights/1)
