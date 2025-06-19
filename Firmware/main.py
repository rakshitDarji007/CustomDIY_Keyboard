import time
import board
import busio
import digitalio
import rotaryio
import usb_hid
import adafruit_matrixkeypad
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode
import adafruit_ssd1306
from adafruit_display_text import label
import terminalio

row_pins = [
    board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13,
    board.GP14, board.GP15
]