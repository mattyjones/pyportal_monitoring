# This file is where you keep secret settings, passwords, and tokens!
# If you put them in the code you risk committing that info or sharing it
# which would be not great. So, instead, keep it all in this one file and
# keep it a secret.

secrets = {
    'ssid' : '',             # Keep the two '' quotes around the name
    'password' : '',         # Keep the two '' quotes around password
    'api_key': '', # This needs to be a sha1 hash of the api secret
    'timezone' : "Africa/Abidjan",  # http://worldtimeapi.org/timezones
    'aio_username' : '', # free, needed for the timestamp https://io.adafruit.com/
    'aio_key' : '', # free, needed for the timestamp https://io.adafruit.com/
    'nightscout_url' : '', # full nightscout url where the data can be found
    'human' : '', # The person being monitored
    }
