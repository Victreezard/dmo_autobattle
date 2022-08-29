import lackey as lk
import json
lk.Settings.MoveMouseDelay = 0.001


class ROIVal():
    def __init__(self, *args):
        if len(args[0]) == 4:
            self.x = args[0][0]
            self.y = args[0][1]
            self.w = args[0][2]
            self.h = args[0][3]


class Action():
    def __init__(self):
        self.x = lk.getX()
        self.y = lk.getY()
        self.w = lk.getW()
        self.h = lk.getH()

    @staticmethod
    def click_low(delay=0.01, repeat=1):
        while repeat > 0:
            lk.mouseDown()
            lk.sleep(delay)
            lk.mouseUp()
            lk.sleep(delay)
            repeat -= 1


if __name__ == "__main__":
    # for property, value in vars(get(522)).items():
    #     print(property, ":", value)
    # with open('dmo.json') as f:
    #     data = json.load(f)
    # rv = ROIVal(data['roi']['farm']['hpBar'])
    # setROI(rv.x, rv.y, rv.w, rv.h)
    a = Action()
    # a.click_low(delay=0.05)
    # sleep(1)
    lk.setROI(800, 400, 400, 150)
    lk.hover(lk.findBest('img/koro5.png'))
    a.click_low()
    a.click_low()
    exit(0)
