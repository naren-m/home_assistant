import json
from os.path import abspath
from os import getcwd
import configparser

# We will use the following Configuration class to read the JSON (http://json.org/) encoded "configuration.json" file.
# This is more user friendly than hardcoding the values in the Python source and only requires minimal changes to one
# file to set up values for your network.


class Config():
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.light_config_file = '/Users/nmudivar/GDrive/python_code/personal/home_assistant/config/configuration.json'
        self.light_config = json.loads(open(self.light_config_file).read())

        self.lightInfoFileName = '/light_info.json'
        self.lightGroupFileName = '/light_groups.json'
        self.lightInfoFile = self.lightInfoFileName
        self.lightGroupFile = self.lightGroupFileName

    def getLightConfigs(self):
        return self.light_config

    def saveLights(self, lightsInfo):
        print("lights data", lightsInfo)
        print("File name", self.lightInfoFile)
        return True

    def saveLightGroups(self, lightGroupsInfo):
        print("light groups data", lightGroupsInfo)
        print("File name", self.lightGroupFile)
        return True
