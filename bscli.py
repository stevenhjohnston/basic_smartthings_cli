import aiohttp
import pysmartthings
import asyncio
from argparse import ArgumentParser
from prettytable import PrettyTable

parser = ArgumentParser()
parser.add_argument("-t", "--token", dest="token",
                    help="Provide a SmartThings App Token.  These are obtained from the SmartThings website - https://account.smartthings.com/tokens")
parser.add_argument("-d", "--deviceid", dest="deviceid",
                    help="Accepted value is a Device ID.  Run bscli.py without arguments to show Device ID list")
parser.add_argument("-c", "--command", dest="command",
                    help="Accepted values are 'on' or 'off' without parenthesis")
args = parser.parse_args()

token = vars(args)['token']
deviceid = vars(args)['deviceid']
command = vars(args)['command']

if token == None:
    print('You must provide a SmartThings API App Token.  Run "bscli.py -h" for help')
    quit()

async def main(token, deviceid, command):
    async with aiohttp.ClientSession() as session:
        api = pysmartthings.SmartThings(session, token)
        devices = await api.devices()

        if deviceid == None or command == None:
            print(f'Device ID: {deviceid} \nCommand: {command}')
            devices_list = []
            for device in devices:
                device_dict = {
                "device_id": device.device_id, 
                "device_name": device.name,
                "device_label": device.label,
                "device_capabilities": device.capabilities
                }
                devices_list.append(device_dict)
            t = PrettyTable(['Device Name', 'Device Label', 'Device ID'])
            for i in devices_list:
                t.add_row([i['device_name'], i['device_label'], i['device_id']])
            print(t)
            print('Provide SmartThings API App Token, Device ID and Command "on" or "off" to switch device on/off.  Run bscli.py -h for help')
        elif (deviceid != None) and (command.upper() == 'ON'):
            index = device_index(deviceid, devices)
            result = await devices[index].switch_on()
            assert result == True
            print (devices[index].label + " Switched ON")
        elif (deviceid != None) and (command.upper() == 'OFF'):
            index = device_index(deviceid, devices)
            result = await devices[index].switch_off()
            assert result == True
            print(devices[index].label + " Switched OFF")
        elif (deviceid != None) and ((command.upper() != 'OFF') or (command.upper() != 'OFF')):
            print('Provide Command "on" or "off"')

def device_index(deviceid, devices):
    device_num = None
    for index, device in enumerate(devices):
        if device.device_id == deviceid:
            device_num = index
    if device_num == None:
        print('device ID not found')
    return device_num

loop = asyncio.get_event_loop()
loop.run_until_complete(main(token, deviceid, command))