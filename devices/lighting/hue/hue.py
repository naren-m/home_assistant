# Required to support the network configuration file
from configuration import Configuration

# Used for printing the Hue exception
import sys

# Coroutine concurrency (http://sdiehl.github.io/gevent-tutorial/#core) imports
import grequests
import gevent

# This method is used as a callback for the asynchronous network communications used to speak to the hub.
# Our version is very simplistic and just outputs the HTTP Response Code to the console.

import json
import http

def printStatus(response, **kwargs):
    print "Hue response was {}".format(response.status_code)

# The following allows us to specify the IP address and username in a more friendly JSON configuration file rather than 
# hardcoding the values in the Python source.

configuration = Configuration()
config = configuration.loadConfig()
print "config", config
hub = config['hue']
http_request = http.Request()

class Hue():
    def turn(self, deviceId='', onOrOff=''):
        if onOrOff == 'on':
            self.turnLightOn(deviceId)
        if onOrOff == 'off':
            self.turnLightOff(deviceId)
    
    def turnLightOn(self, deviceId):
        # The grequests library sends the request as soon as we create "job" below. We then yield to the greenlet every hundredth of a second
        # in the main update method to ensure we capture the result.
        req_url = 'http://{ip}/api/{username}/lights/{devId}/state'.format(
            ip=hub['IP'],
            username=hub['username'],
            devId=deviceId)
        print "req_url", req_url
        req = http_request.put(
            req_url,
            data=dict({"on":True ,"bri":254}))

    def turnLightOff(self, deviceId):
        # The grequests library sends the request as soon as we create "job" below. We then yield to the greenlet every hundredth of a second
        # in the main update method to ensure we capture the result.
        req_url = 'http://{ip}/api/{username}/lights/{devId}/state'.format(
            ip=hub['IP'],
            username=hub['username'],
            devId=deviceId)
        print "req_url", req_url
        req = http_request.put(
            req_url,
            data=dict({"on":False ,"bri":254}))
