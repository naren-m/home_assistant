#!/usr/local/bin/python3
"""
CLI module to control philips hue lights.
"""
import click
# import utils
from devices.lighting.hue import hue


def action_on_light_by_id(light_id, action):
    """
    Action on one light by light_id.
    """
    h = hue.Hue()
    if action == 'on':
        h.turn(light_id, h.LIGHT_STATE_ON)
    elif action == 'off':
        h.turn(light_id, h.LIGHT_STATE_OFF)
    elif action == 'toggle':
        h.toggle(light_id)


@click.command(name="Hue CLI")
@click.option('--id', help='ID of philips hue light.')
@click.option('--action', type=click.Choice(['on', 'off', 'toggle']))
def control_lights(id, action):
    print(action)
    if id == "" or id is None:
        return
    else:
        action_on_light_by_id(id, action)


# click.echo(id)
# status, light = h.getLightDetails(id)
# if status != 200:
#     click.secho('Failed to get light with id %s!' % id, fg='red')
# state = h.toggle(id)
# click.secho('Turning %s light %s!' % (light['name'], state), fg='green')
# utils.print_json_obj(light)

if __name__ == '__main__':
    control_lights(id, "")