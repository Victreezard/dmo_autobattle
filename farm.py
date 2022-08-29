import threading
from keyboard import is_pressed
import lackey as lk

lk.Settings.MoveMouseDelay = 0.001


class Action():
    def __init__(self):
        self.moveFlag = True
        self.x = lk.getX()
        self.y = lk.getY()
        self.w = lk.getW()
        self.h = lk.getH()

        self.newAtt = 'img/newAtt.png'
        self.yes = 'img/yes.png'

    @staticmethod
    def press(char, delay=0.005, repeat=1):
        while repeat > 0:
            lk.keyDown(char)
            lk.sleep(delay)
            lk.keyUp(char)
            lk.sleep(delay)
            repeat -= 1

    @staticmethod
    def click_low(delay=0.01, repeat=1):
        while repeat > 0:
            lk.mouseDown()
            lk.sleep(delay)
            lk.mouseUp()
            lk.sleep(delay)
            repeat -= 1

    def farm(self):
        lk.setROI(820, 47, 175, 25)
        while True:
            self.press('3', delay=1, repeat=2)
            if is_pressed('escape'):
                break
            self.press('{TAB}')
            self.press('5', delay=1)
            self.press('3')
            if not lk.exists('img/hpBar.png'):
                if self.moveFlag:
                    self.press('a', 0.7)
                else:
                    self.press('d', 0.7)
                self.moveFlag = not self.moveFlag
                continue

    def attack(self):
        while True:
            if is_pressed('escape'):
                break
            self.press('{TAB}')
            self.press('1')
            lk.sleep(0.01)
            self.press('2')
            lk.sleep(1)

    def pick_up(self):
        while True:
            if is_pressed('escape'):
                break
            self.press('2')
            lk.sleep(0.8)

    def discard_att(self):
        while True:
            if is_pressed('escape'):
                break
            lk.setROI(1520, 680, 375, 175)
            try:
                if lk.findBest(self.newAtt):
                    lk.mouseMove()
                    self.click_low(0.1)
            except Exception:
                lk.sleep(5)
                continue
            lk.mouseMove(lk.setRect(self.w / 2, self.h / 2, 50, 50))
            self.click_low(0.1)
            lk.setROI(860, 370, 100, 50)
            lk.hover(self.yes)
            self.click_low(0.1)


if __name__ == "__main__":
    a = Action()
    attack = threading.Thread(target=a.attack)
    pick_up = threading.Thread(target=a.pick_up)
    discard_att = threading.Thread(target=a.discard_att)

    attack.start()
    pick_up.start()
    discard_att.start()

    attack.join()
    pick_up.join()
    discard_att.join()

    exit(0)
