# basic_smartthings_cli

## Description

Basic CLI tool using pysmartthings to interact with your SmartThings devices.

Created for use with OctoPrint running on OctoPi but it can be used for anything where you want to switch devices on or off using Python.  You must obtain a Personal Access Token for the SmartThings API before use.

When bscli.py is used with the *System Command Editor* (https://plugins.octoprint.org/plugins/systemcommandeditor/) plug-in it provides an easy way to control your SmartThings compatible devices directly from the OctoPrint GUI.  
For example, this can be used to power on/off your 3D printer and LEDs from inside the OctoPrint GUI.

## Installation

1. Clone the repo.  If installing on OctoPi, you can do this into the home directory (~ or /home/pi).  
    `git clone https://github.com/stevenhjohnston/basic_smartthings_cli.git`
  
2. Install dependencies using pip.  
- If installing on OctoPi you might find trying to use pip returns an error, to overcome this you can use the pip installed with OctoPrint by using the full path *~/oprint/bin/pip*  
- If you also want to install dependencies into the newly created **basic_smartthings_cli** folder and not the OctoPrint Python folders to keep it totally separate include target in the command and select the directory.  
Using `-t .` will install into the current working directory so make sure to change directory using `cd` into the new folder using before running pip to deploy there.  
  `cd basic_smartthings_cli`  
  `~/oprint/bin/pip install -r requirements.txt -t .`  

- If not installing on OctoPi use the command below.  
    `pip install -r requirements.txt`

## Running bscli.py

If you have not already obtained a SmartThings Personal access token visit https://account.smartthings.com/tokens and generate one, you will need it to run this tool.

If running on OctoPi you can execute using the full path.  For running from **/home/pi/basic_smartthings_cli** run the below  
`python3 /home/pi/basic_smartthings_cli/bscli.py`
  
If running elsewhere execute from inside the directory as usual  
`python bscli.py`

## Arguments
- Running without arguments will return the following  
>You must provide a SmartThings API App Token.  Run "bscli.py -h" for help

- **-h** will provide help.

- **-t** is used to provide the SmartThings API Personal Access Token

- **-d** is used for providing the device ID you wish to interact with.  See below for listing Device IDs.

- **-c** is used for providing a command of either *on* or *off*

## Listing Devices
Run bscli.py with the token argument and provide your SmartThings API Personal Access Token.  This will provide a table of your devices.  
`python bscli.py -t <Personal Access Token>`

## Switching Devices On or Off
Run bscli.py with the token argument, the Device ID (listed using the above approach) along with either "on" or "off"  
`python bscli.py -t <Personal Access Token> -d <Device ID> -c on`  
`python bscli.py -t <Personal Access Token> -d <Device ID> -c off`

## OctoPi Run Examples
- To list devices on an OctoPi use the below command  
`python3 /home/pi/basic_smartthings_cli/bscli.py -t <SmartThings_Token>`

- To switch on a device listed from the previous command  
`python3 /home/pi/basic_smartthings_cli/bscli.py -t <SmartThings_Token> -d <Device ID> -c on`

- To switch off a device listed from the previous command  
`python3 /home/pi/basic_smartthings_cli/bscli.py -t <SmartThings_Token> -d <Device ID> -c off`