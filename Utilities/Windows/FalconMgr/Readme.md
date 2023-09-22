# FalconMgr

FalconMgr is a command line utility for managing the configuration of one or more Falcon controllers from batch scripts. This can make it really easy to manage larger displays and particularly larger commercial displays with configurations duplicated in multiple locations.

Some of the key features:
- Able to backup configurations
- Able to generate configurations from xLights in bulk
- Able to convert configurations between V3, V4 and V5 falcon controllers (where compatible)
- Able to upgrade V4 and V5 firmware

As a command line utility it can be scripted into CMD files for repeatable actions.

The command line options

`-h` Display command line help. If no `-c` options is specified then it is the high level syntax. If `-c` is specified then it is the syntax for that command.
`-t` This provides additional tracing information when the program is interacting with controllers. Useful for debugging mostly.
`-p` When specified FalconMgr will pause when done and wait for a key press.
`-b <brandname>` When run FalconMgr displays the Falcon branding in large green letters. Use this option to replace that branding with your own.
`-c <command>` Specifies the action to be taken by FalconMgr. Only one action can be taken per execution (although that action can run against many controllers).
`-ct <filename.json>` For commands which can work against multiple controllers this option specifies the file that will list the controllers to act upon. Some commands such as `discover` will create this file.
`-ip <ip>` For commands which can run against a single controller this is the IP address of the controller to use. Generally you use `-ip` or `-ct`
`-f <folder>` When uploading/downloading configurations this is the folder you want FalconMgr to store the configurations in.
`-s <filename>` This option specifies the file falconmgr should use. Depending on the command it may be used differently. In the case of `upload` it is the configuration file to use and is optional (as there is a default). In the case of `sendfile` its the file to send.
`-x <xlights show folder` This option is used when generating controller configurations from xlights

When FalconMgr runs it will set the ERRORLEVEL on exit as follows:
- `0` - Success
- `1` - Partial failure
- `2` - Serious failure

## Examples of usage

### Generate Controller Configurations From xLights

`FalconMgr.exe -c generate -x "c:\show folder" -f "c:\controller configurations" -ip 192.168.1.50`

Generate the controller configuration into the "c:\controller configurations" folder for the 192.168.1.50 controller only.

### Discover all controllers

`FalconMgr.exe -c discover -ct controllers.json`

Create a controllers.json file containing a list of all the controllers currently online.

### Upload new firmware to all the controllers discovered

`FalconMgr.exe -c sendfile -s firmware.fl3 -ct controllers.json`

### Backup the configuration of all my controllers

`FalconMgr.exe -c download -ct controllers.json -f "c:\controller configuration backups"`

### Update all my controller configurations to the last backed up configuration

`FalconMgr.exe -c upload -ct controllers.json -f "c:\controller configuration backups"`
