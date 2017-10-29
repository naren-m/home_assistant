import json
from os.path import abspath
from os import getcwd

# We will use the following Configuration class to read the JSON (http://json.org/) encoded "configuration.json" file.
# This is more user friendly than hardcoding the values in the Python source and only requires minimal changes to one
# file to set up values for your network.


class Config():
    def __init__(self):
        self.configFileName = '/configuration.json'
        self.lightInfoFileName = '/light_info.json'
        self.lightGroupFileName = '/light_groups.json'
        self.configFile = abspath(getcwd() + self.configFileName)
        self.lightInfoFile = abspath(getcwd() + self.lightInfoFileName)
        self.lightGroupFile = abspath(getcwd() + self.lightGroupFileName)

    def loadConfig(self):
        config = json.loads(open(self.configFile).read())
        return config

    def saveLights(self, lightsInfo):
        print("lights data", lightsInfo)
        print("File name", self.lightInfoFile)
        return True

    def saveLightGroups(self, lightGroupsInfo):
        print("light groups data", lightGroupsInfo)
        print("File name", self.lightGroupFile)
        return True
