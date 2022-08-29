from keyboard import add_hotkey, wait
from lackey import exit, getLastMatch, hover, keyDown, keyUp, mouseDown, mouseUp, sleep, Settings

Settings.MoveMouseDelay = 0.01

class Action():
    def __init__(self):
        self.roundFlag = True
        self.start = 'img/colo/round.png'
        self.startLoc = None
        self.quickStart = 'img/colo/quickRound.png'
        self.quickStartLoc = None

    @staticmethod
    def press(char, delay=0.01, repeat=1):
        while repeat > 0:
            keyDown(char)
            sleep(delay)
            keyUp(char)
            sleep(delay)
            repeat -= 1

    @staticmethod
    def click_low(delay=0.01, repeat=1):
        while repeat > 0:
            mouseDown()
            sleep(delay)
            mouseUp()
            sleep(delay)
            repeat -= 1

    def prep_round(self):
        self.press('{SPACE}')
        self.press('w')

    def start_round(self):
        self.press('{SPACE}')
        if self.startLoc != None:
            hover(self.startLoc)
        else:
            hover(self.start)
            self.startLoc = getLastMatch()
        self.click_low(0.1, 3)

    def start_quick_round(self):
        if self.quickStartLoc != None:
            hover(self.quickStartLoc)
        else:
            try:
                hover(self.quickStart)
                self.quickStartLoc = getLastMatch()
            except Exception:
                pass
        self.click_low(0.1, 3)

    def advance_round(self):
        if self.roundFlag:
            self.prep_round()
        else:
            try:
                self.start_round()
            except Exception:
                pass
        self.roundFlag = not self.roundFlag


if __name__ == "__main__":
    a = Action()
    add_hotkey('u', a.advance_round)
    add_hotkey('q', a.start_quick_round)
    wait('0')
    exit(0)
