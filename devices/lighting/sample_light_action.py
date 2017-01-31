import hue

h = hue.Hue()

h.toggle(2)

h.saveLightsToConfig()

h.saveGroupsToConfig()
