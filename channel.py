from keyboard import wait
from lackey import exists, hover, keyDown, keyUp, mouseDown, mouseUp, sleep, Settings
from sys import exit
Settings.MoveMouseDelay = 0.01


class Action():

    def __init__(self):
        pass

    @staticmethod
    def press(char, delay=0.05):
        keyDown(char)
        sleep(delay)
        keyUp(char)

    @staticmethod
    def click_low(delay=0.05):
        mouseDown()
        sleep(delay)
        mouseUp()

    def change_channel(self, channel=0):
        wait('up')
        hover('img/channel/channelButton.png')
        self.click_low()
        sleep(0.5)
        hover(f"img/channel/channel{channel}.png")
        self.click_low()
        self.press('{ENTER}')


if __name__ == "__main__":
    a = Action()
    channel = 0
    while True:
        try:
            a.change_channel(channel)
        finally:
            continue
        if channel < 2:
            channel += 1
        else:
            channel = 0
    exit(0)
