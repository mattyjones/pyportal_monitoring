# T1D Monitoring with a Pyportal

![License](https://img.shields.io/github/license/mattyjones/pyportal_monitoring.svg)![Date](https://img.shields.io/github/release-date/mattyjones/pyportal_monitoring.svg)![Releases](https://img.shields.io/github/downloads/mattyjones/pyportal_monitoring/0.0.1/total.svg)

![Twitter](https://img.shields.io/twitter/follow/caffeinatedeng.svg?style=social)

![img](https://pbs.twimg.com/media/D4TDQhIWkAA4Dih.jpg:small)


This uses an [AdaFruit Pyportal][1] to display the latest blood sugar from [Nightscout][2] along with a name and the current trend. The background color is determined by the current level and gives a quick visual as to the current state.

## Prerequisites
- A pyportal
- A usb cable capable of transmitting data
- A wifi connection
- This requires version 4 of circuit python. You can download the latest file and install it using these [instructions][3].
- A functioning nightscout site

## Installation

Once you have installed circuitpython copy the following to the **CIRCUITPY** folder. 

- lib/
- fonts/
- code.py
- secrets.py
- pyportal_startup.bmp
- pyportal_startup.wav

You will also need to edit the secrets.py file and fill in the necessary configuration pieces. If your nightscout site has auth you will need to add the SHA1 hash of the secret as well. This can be ignored otherwise. The file contains further details.

The pyportal will automatically restart and if everything is configured properly then it should work.

## Usage

The name displayed can be set in *secrets.py* and the position can be adjusted on the screen following the comments in *code.py*.

The background will change based on alert levels and will go purple if the data coming back from nightscout is stale (over a given threshold). These values can all be adjusted in *code.py*.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)


[1]: https://www.adafruit.com/product/4116
[2]: https://github.com/nightscout/cgm-remote-monitor
[3]: https://learn.adafruit.com/adafruit-pyportal/install-circuitpython
