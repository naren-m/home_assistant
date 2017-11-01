import sys
import json

from utils import http
from config import config


class Hue():
    def __init__(self):
        """
            Class variables
        """
        self.configuration = config.Config()
        self.configs = self.configuration.getLightConfigs()
        self.hub = self.configs['hue']
        self.http_request = http.Request()
        self.HUE_GET_LIGHTS_ALL = 'http://{ip}/api/{username}/lights'
        self.HUE_GET_LIGHTS = 'http://{ip}/api/{username}/lights/{devId}'
        self.HUE_PUT_LIGHTS = 'http://{ip}/api/{username}/lights/{devId}/state'
        self.HUE_GET_GROUPS = 'http://{ip}/api/{username}/groups'
        self.HUE_GET_SCENES = 'http://{ip}/api/{username}/scenes'
        self.LIGHT_STATE_ON = 'on'
        self.LIGHT_STATE_OFF = 'off'

    def _getPutUrl(self, deviceId):
        req_url = self.HUE_PUT_LIGHTS.format(
            ip=self.hub['IP'], username=self.hub['username'], devId=deviceId)
        return req_url

    def _geGetAllLightsUrl(self):
        get_url = self.HUE_GET_LIGHTS_ALL.format(
            ip=self.hub['IP'], username=self.hub['username'])
        return get_url

    def _getGetLightDetailsUrl(self, deviceId):
        get_url = self.HUE_GET_LIGHTS.format(
            ip=self.hub['IP'], username=self.hub['username'], devId=deviceId)
        return get_url

    def _getGroupsUrl(self):
        get_url = self.HUE_GET_GROUPS.format(
            ip=self.hub['IP'], username=self.hub['username'])
        return get_url

    def _get(self, url):
        resp = self.http_request.get(url)
        return resp

    def getAllGroups(self):
        resp = self._get(self._getGroupsUrl())
        return resp.status_code, resp.json()

    def getAllLights(self):
        resp = self._get(self._geGetAllLightsUrl())
        return resp.status_code, resp.json()

    def getLightDetails(self, deviceId):
        """
        Get the light details

        input  : deviceId
        output : returns light data in json format

        Sample output -
            {
                "name": "Living room hanging",
                "state": {
                    "on": true,
                    ...
                },
                "type": "Extended color light",
            }
        """
        get_url = self._getGetLightDetailsUrl(deviceId)
        resp = self._get(get_url)
        return resp.status_code, resp.json()

    def put(self, url, payload):
        req = self.http_request.put(url, data=payload)
        return req

    def toggle(self, deviceId):
        """
        Get the status of  light and toggle it
        """
        current_state = None
        resp, lightData = self.getLightDetails(deviceId)

        if lightData['state'][self.LIGHT_STATE_ON]:
            self.turnDeviceOff(deviceId)
            current_state = self.LIGHT_STATE_OFF
        else:
            self.turnDeviceOn(deviceId)
            current_state = self.LIGHT_STATE_ON

        return current_state

    def turn(self, deviceId='', onOrOff=''):
        if onOrOff == self.LIGHT_STATE_ON:
            self.turnDeviceOn(deviceId)
        if onOrOff == self.LIGHT_STATE_OFF:
            self.turnDeviceOff(deviceId)

    def turnDeviceOn(self, deviceId):
        req_url = self._getPutUrl(deviceId)
        req = self.put(req_url, payload=dict({"on": True, "bri": 254}))

    def turnDeviceOff(self, deviceId):
        req_url = self._getPutUrl(deviceId)
        req = self.put(req_url, payload=dict({"on": False, "bri": 254}))

    def saveLights(self):
        lightsJson = self.getAllLights()
        ret = self.configuration.saveLights(lightsJson)
        return ret

    def saveGroups(self):
        lightGroupsJson = self.getAllGroups()
        ret = self.configuration.saveLightGroups(lightGroupsJson)
        return ret
