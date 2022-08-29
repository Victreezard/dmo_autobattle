import json
import mouse
import pprint
from time import sleep

class Mouser:
    def __init__(self):
        self.points_filename = "points.json"
        self.points = {}
        self.default_points = {
            "attack": [0, 0],
            "target": [0, 0],
            "skill_1": [0, 0],
            "skill_2": [0, 0],
            "pick_up": [0, 0]
        }

        try:
            self.points = self._load_points(self.points_filename)
        except FileNotFoundError:
            self._overwrite_points(self.points_filename, self.default_points)
            print(f'{self.points_filename} was not found. A new file was created with default values.')
            self.points = self._load_points(self.points_filename)

    @staticmethod
    def _overwrite_points(points_filename, points):
        with open(points_filename, 'w+') as points_file:
            json.dump(points, points_file)

    @staticmethod
    def _load_points(points_filename):
        points = {}
        with open(points_filename) as points_file:
            points = json.load(points_file)
        return points

    def record_points(self):
        for name in self.points:
            input(f'Press ENTER to record {name.upper()} mouse point')
            self.points[name] = list(mouse.get_position())
        self._overwrite_points(self.points_filename, self.points)
        print('New points recorded:')
        pprint.pprint(self.points, sort_dicts=False)

    def click_point(self, point):
        mouse.move(point[0], point[1], absolute=False, duration=.5)
        mouse.double_click('left')
        sleep(0.5)

if __name__ == "__main__":
    from ahk import AHK

    ahk = AHK()
    sleep(3)
    ahk.type('aaa')
    # mouser = Mouser()
    # mouser.record_points()
    # sleep(4)
    # for name in mouser.points:
    #     mouser.click_point(mouser.points[name])
