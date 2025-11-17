# Falcon F16/F48 V4 Frequently Asked Questions/Issues

Please see the manual https://docs.google.com/document/d/1449zGk1HEiQjcu6e98ebWnFBMFKUiXaFzis9QGAnfsk/edit 

## Ports 17-32 Not Working on a F48

When the controller is in 32 port mode to get 1024 pixels per output Ports 17-32 are actually Ports 33-48 on the board. This is to allow the user to use the onboard receiver.

## Playback stops when playing a sequence from the SD Card

The most common reason we have seen for this is not using a sufficiently high quality SD Card. We recommend 8-32GB SanDisk Class 10 SD Cards. Other cards will likely work but we have seen issues with cheaper no-name cards. When the issue occurs the sequence will just stop playing part way through and may display a timeout if you have logging turned on.

## Controller Status Page Has Blank Board Type

The best fix for this is to factory reset the controller by applying power while the select button is held down.

## Controller OLED does not display anything when power is applied

The most common reasons for this are:

- Applying 5V but having the voltage selector set to 12V.
- Having the External power switch set incorrectly.

## Network Green/Amber Lights dont light when network is connected

Verify you have plugged the internet into one of the two silver RJ45 connectors with the black insides.

## LOR/DMX Devices not seeing a signal

Verify all 3 jumpers next to the DMX RJ45 port are set to the right position.

## Wifi Web Page Returns 404 Errors

Install/Reinstall the latest V4 firmware.

## TM1814 pixels flicker

This definitely can happen if you have more pixels attached than the controller is driving so please make sure you are sending data to all pixels.
If you have other issues contact us at support@pixelcontroller.com.


