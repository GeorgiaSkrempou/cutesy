from grove.factory import Factory
import time
from textwrap import wrap
import requests
from datetime import datetime
import pytz
import datetime
DISPLAY_ID = 'JHD1802'

display = Factory.getDisplay(DISPLAY_ID)
display.clear()



cute_messages = ['Hey lil\' bug, I love you']
cute_messages.append('Hakuna matata!')

for message in range(0,len(cute_messages)):
    cute_messages[message] = 15*' '+cute_messages[message]+' '

for message in range(0,len(cute_messages)):
    for letter in range(0, len(cute_messages[message])):
        display.clear()
        
        display.write(cute_messages[message][letter:len(cute_messages[message])])
        time.sleep(0.5)
