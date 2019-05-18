import time
import board
from adafruit_pyportal import PyPortal

try:
    from secrets import secrets
except ImportError:
    print("WiFi and API secrets are kept in secrets.py, please add them there!")
    raise

# Set up where we'll be fetching data from
DATA_SOURCE = secrets['nightscout_url']
BG_VALUE = [0, 'sgv']
BG_DIRECTION = [0, 'direction']
DATA_AGE = [0, 'date']

# Display Colors
RED = 0xFF0000;     # CRIT HIGH, CRIT LOW
ORANGE = 0xFFA500;  # WARN LOW 
YELLOW = 0xFFFF00;  # WARN HIGH
GREEN = 0x00FF00;   # BASE
PURPLE = 0x800080;  # STALE DATA
BLACK = 0x000000;   # TEXT

# Alert Levels
CRIT_HIGH = 280
WARN_HIGH = 180
CRIT_LOW = 60
WARN_LOW = 80

def stale_data(timestamp):

    # stale results is the age at which results are no longer considered valid.
    # This is in minutessd
    stale_time = 6

    # Get the current timestamp in GMT
    epoch_time = time.time()
    print("Epoch GMT time:", epoch_time)

    current_time_str = str(timestamp)

    current_time_str = current_time_str[:-3] # nightscout sends a higher percision then is necessary and does not use dot notation
    current_time_int = int(current_time_str)

    # The number of minutes ago that the data was last checked
    last_check = (epoch_time - current_time_int) /60
    print("Data age: ", last_check)

    if last_check > stale_time:
        return True
    else:
        return False
    
    # In the case where we have no idea, don't trust the data
    return True

def get_bg_color(val, timestamp):
    if stale_data(timestamp):
        return PURPLE
    else:    
        if val > CRIT_HIGH:
            return RED
        elif val > WARN_HIGH:
            return YELLOW
        elif val < CRIT_LOW:
            return RED
        elif val < WARN_LOW:
            return ORANGE
        return GREEN

def text_transform_bg(val):

    # If you are outside the US you may want to change this
    return str(val) + ' mg/dl' 

def text_transform_direction(val):
    if val == "Flat":
        return "→"
    if val == "SingleUp":
        return "↑"
    if val == "DoubleUp":
        return "↑↑"
    if val == "DoubleDown":
        return "↓↓"
    if val == "SingleDown":
        return "↓"
    if val == "FortyFiveDown":
        return "→↓"
    if val == "FortyFiveUp":
        return "→↑"
    return val

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE,
                    headers={'api-secret': secrets['api_key']}, # If you don't have auth on your site you can ignore this
                    caption_text=secrets['human'], # Name of the person you are following
                    caption_position=(100, 80), # This is going to be subjective to the length of the name
                    caption_font=cwd+"/fonts/Arial-Bold-24-Complete.bdf",
                    caption_color=BLACK, # Black text is easier to read, feel free to change it
                    json_path=(BG_VALUE, BG_DIRECTION, DATA_AGE),
                    status_neopixel=board.NEOPIXEL,
                    default_bg=0xFFFFFF,
                    text_font=cwd+"/fonts/Arial-Bold-24-Complete.bdf",
                    text_position=((90, 120),  # VALUE location
                                   (140, 160)), # DIRECTION location
                    text_color=(BLACK,  # sugar text color
                                BLACK), # direction text color
                    text_wrap=(35, # characters to wrap for sugar
                               0), # no wrap for direction
                    text_maxlen=(180, 30), # max text size for sugar & direction
                    text_transform=(text_transform_bg,text_transform_direction),
                   )

# speed up projects with lots of text by preloading the font!
pyportal.preload_font(b'mg/dl012345789');
pyportal.preload_font((0x2191, 0x2192, 0x2193))

while True:
    try:
        value = pyportal.fetch()
        print("Getting time from internet!")
        pyportal.get_local_time(location="Africa/Abidjan")
        pyportal.set_background(get_bg_color(value[0], value[2]))
        print("Response is", value)

    except RuntimeError as e:
        print("An error occured, retrying! -", e)
    time.sleep(180)

