import sys
import json

import respond

from utils import http
# Required to support the network configuration file
from configuration import Configuration

class Hue():
    def __init__(self):
        """
            Class variables
        """
        configuration = Configuration()
        self.configs = configuration.loadConfig()
        self.hub = self.configs['hue']
        self.http_request = http.Request()
        self.HUE_GET_LIGHTS_ALL = 'http://{ip}/api/{username}/lights'
        self.HUE_GET_LIGHTS     = 'http://{ip}/api/{username}/lights/{devId}'
        self.HUE_PUT_LIGHTS     = 'http://{ip}/api/{username}/lights/{devId}/state'
        self.HUE_GET_GROUPS       = 'http://{ip}/api/{username}/groups'
        self.HUE_GET_SCENES     = 'http://{ip}/api/{username}/scenes'
        self.respond = respond.Respond()

    def put(self, url, payload):
        req = self.http_request.put(url, data=payload)
        return req

    def get(self, url):
        req = self.http_request.get(url)
        return req

    def getPutUrl(self, deviceId):
        req_url = self.HUE_PUT_LIGHTS.format(
            ip=self.hub['IP'],
            username=self.hub['username'],
            devId=deviceId)
        return req_url

    def geGetAllLightsUrl(self):
        get_url = self.HUE_GET_LIGHTS_ALL.format(
            ip=self.hub['IP'],
            username=self.hub['username'])
        return get_url

    def getGetLightDetailsUrl(self, deviceId):
        get_url = self.HUE_GET_LIGHTS.format(
            ip=self.hub['IP'],
            username=self.hub['username'],
            devId=deviceId)
        return get_url

    def getGroupsUrl(self):
        get_url = self.HUE_GET_GROUPS.format(
            ip=self.hub['IP'],
            username=self.hub['username'])
        return get_url

    def  toggle(self, deviceId):
        """
        Get the status of  light and toggle it
        """
        lightData = self.getLightDetails(deviceId)
        if lightData['state']['on']:
            self.turnLightOff(deviceId)
            self.respond.response( lightData['name'], "is on. Turning it off")
        else:
            self.turnLightOn(deviceId)
            self.respond.response( lightData['name'], "is off. Turning it on")

    def turn(self, deviceId='', onOrOff=''):
        if onOrOff == 'on':
            self.turnLightOn(deviceId)
        if onOrOff == 'off':
            self.turnLightOff(deviceId)

    def turnLightOn(self, deviceId):
        req_url = self.getPutUrl(deviceId)
        req = self.put( req_url, payload=dict({"on":True ,"bri":254}))

    def turnLightOff(self, deviceId):
        req_url = self.getPutUrl(deviceId)
        req = self.put( req_url, payload=dict({"on":False ,"bri":254}))

    def getAllGroups(self):
        get_url = self.getGroupsUrl()
        response = self.get(get_url)
        return response[1]

    def getAllLights(self):
        get_url = self.geGetAllLightsUrl()
        req = self.get(get_url)
        return req[1]

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
        get_url = self.getGetLightDetailsUrl(deviceId)
        req =  self.get(get_url)
        return req[1]

