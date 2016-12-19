# Required to support the network configuration file
from configuration import Configuration

# Used for printing the Hue exception
import sys
import json
from utils import http

def printStatus(response, **kwargs):
    print "Hue response was {}".format(response.status_code)


class Hue():
    def __init__(self):
        """
            Class variables
        """
        configuration = Configuration()
        self.configs = configuration.loadConfig()
        self.hub = self.configs['hue']
        self.http_request = http.Request()
        self.HUE_GET_URL_ALL = 'http://{ip}/api/{username}/lights'
        self.HUE_GET_URL = 'http://{ip}/api/{username}/lights/{devId}'
        self.HUE_PUT_URL = 'http://{ip}/api/{username}/lights/{devId}/state'
        print "config", self.configs

    def put(self, url, payload):
        req = self.http_request.put(url, data=payload)
        return req

    def get(self, url):
        req = self.http_request.get(url)
        return req

    def getHuePutUrl(self, deviceId):
        req_url = self.HUE_PUT_URL.format(
            ip=self.hub['IP'],
            username=self.hub['username'],
            devId=deviceId)
        return req_url

    def getHueGetAllUrl(self):
        get_url = self.HUE_GET_URL_ALL.format(
            ip=self.hub['IP'],
            username=self.hub['username'])
        return get_url

    def getHueGetDeviceUrl(self, deviceId):
        get_url = self.HUE_GET_URL.format(
            ip=self.hub['IP'],
            username=self.hub['username'],
            devId=deviceId)
        return get_url

    def  toggle(self, deviceId=''):
        """
        Get the status of  light and toggle it
        """
        pass

    def turn(self, deviceId='', onOrOff=''):
        if onOrOff == 'on':
            self.turnLightOn(deviceId)
        if onOrOff == 'off':
            self.turnLightOff(deviceId)

    def turnLightOn(self, deviceId):
        req_url = self.getHuePutUrl(deviceId)
        req = self.put( req_url, payload=dict({"on":True ,"bri":254}))

    def turnLightOff(self, deviceId):
        req_url = self.getHuePutUrl(deviceId)
        req = self.put( req_url, payload=dict({"on":False ,"bri":254}))

    def getAllHueLights(self):
        get_url = self.getHueGetAllUrl()
        req = self.http_request.get(get_url)
        return req

    def getHueLightDetails(self, deviceId):
    	"""
    	Get the light details

    	input  : deviceId
    	output : returns light data in json format

    	Sample output -
    	    {
    	    	"name": "Living room hanging",
    	    	"swversion": "5.50.1.19085",
    	    	"manufacturername": "Philips",
    	    	"state": {
    	    		"on": true,
    	    		"hue": 34076,
    	    		"colormode": "xy",
    	    		"effect": "none",
    	    		"alert": "none",
    	    		"xy": [0.3144, 0.3301],
    	    		"reachable": true,
    	    		"bri": 254,
    	    		"ct": 153,
    	    		"sat": 251
    	    	},
    	    	"uniqueid": "00:17:88:01:10:56:f7:13-0b",
    	    	"type": "Extended color light",
    	    	"modelid": "LCT007"
    	    }
    	"""
        get_url = self.getHueGetDeviceUrl(deviceId)
        req =  self.get(get_url)
        return req[1]

