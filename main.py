from pyautogui import scroll
from keyboard  import add_hotkey as addHotkey

from time import sleep


def scrollUp   () : scroll( 100)
def scrollDown () : scroll(-100)

addHotkey('alt+up'  , scrollUp)
addHotkey('alt+down', scrollDown)

while 1 : pass