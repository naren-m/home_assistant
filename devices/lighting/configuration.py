import json
import hue
from os.path import abspath
from os import getcwd


# We will use the following Configuration class to read the JSON (http://json.org/) encoded "configuration.json" file.
# This is more user friendly than hardcoding the values in the Python source and only requires minimal changes to one
# file to set up values for your network.


class Configuration():
    def __init__(self):
        self.configFileName = '/configuration.json'
        self.configFile = abspath(getcwd() + self.configFileName)

    def loadConfig(self):
        config = json.loads( open(self.configFile).read())
        return config

    def saveLightsConfig(self):
        pass

    def saveLightGroupConfig(self):
        pass
c = Configuration()
c.saveLightGroupConfig()
