import sys, traceback

from configuration import Configuration

from hue import Hue


def runMain():
    # First, we import our devices from our configuration file. These will be split into two different groups, those
    # controlled by Philips Hue and those controlled by Insteon.
    configuration = Configuration()
    config = configuration.loadConfig()

    hueDevices = {}

    for device in config['devices']['hue']:
        hueDevices[device] = config['devices']['hue'][device]
    hue = Hue()

    # We want to run forever, or until the user presses control-c, whichever comes first.
    # while True:
    try:
        command = "turn on the living room light"
        command = command.replace('the', '')
        print command
        if command.startswith('turn'):
            onOrOff = command.split()[1]
            deviceName = ''.join(command.split()[2:])
            print deviceName
            print hueDevices
            if deviceName in hueDevices:
                deviceId = hueDevices[deviceName]['deviceID']
                print deviceId
                hue.turn(deviceId=deviceId, onOrOff=onOrOff)

    except (KeyboardInterrupt, SystemExit):
        print 'People sometimes make mistakes, Goodbye.'
        sys.exit()
    except Exception as e:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback,
                                  limit=2,
                                  file=sys.stdout)
        sys.exit()


if __name__ == '__main__':
    runMain()
