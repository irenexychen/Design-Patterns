__author__ = 'Xiang-Yi'

class MoppingRobot:
    def doJob(self, roomCleaniness, key):
        roomCleaniness.RoomCleaniness()[key] = "0"
        return ("Location %s was mopped" %(key))

    def __str__(self):
        return "Mopping Robot called."


class SweepingRobot:
    def doJob(self, roomCleaniness, key):
        roomCleaniness.RoomCleaniness()[key] = "0"
        return ("Location % was sweeped" %(key))

    def __str__(self):
        return "Sweeping Robot called."


class Cleaniness():
    _roomCleaniness = {}

    def __init__(self, **kwargs):
        with open("house_data.txt") as f:
            for line in f:
                (key, val) = line.split()
                self._roomCleaniness[key] = val
        self.TotalHouse = len(self._roomCleaniness)


    def __str__(self):
        return str(self._roomCleaniness)

    def RoomCleaniness(self):
        return self._roomCleaniness

    def printDic(self):
        for key in self._roomCleaniness:
            print(key, self._roomCleaniness[key])


class Management():
    def needToMop(self, totalHouse, roomCleaniness):
        mop = 0
        for k in roomCleaniness.RoomCleaniness():
            if roomCleaniness.RoomCleaniness()[k] == "M":
                mop = mop + 1
        if mop >= (totalHouse*0.3):
            return True


    def needToSweep(self, totalHouse, roomCleaniness):
        sweep = 0
        for k in roomCleaniness.RoomCleaniness():
            if roomCleaniness.RoomCleaniness()[k] == "S":
                sweep = sweep + 1
        if sweep >= (totalHouse*0.3):
            return True


    def checkToMop(self, MoppingRobot, roomCleaniness):
        for k in roomCleaniness.RoomCleaniness().keys():
            if roomCleaniness.RoomCleaniness()[k] == "M":
                MoppingRobot.doJob(roomCleaniness, k)


    def checkToSweep(self, SweepingRobot, roomCleaniness):
        for k in roomCleaniness.RoomCleaniness().keys():
            if roomCleaniness.RoomCleaniness()[k] == "S":
                SweepingRobot.doJob(roomCleaniness, k)



houseOne = Cleaniness();

houseOneManager = Management();
Mopper = MoppingRobot();
Sweeper = SweepingRobot();

if houseOneManager.needToMop(houseOne.TotalHouse, houseOne) == True:
    houseOneManager.checkToMop(Mopper, houseOne)

if houseOneManager.needToSweep(houseOne.TotalHouse, houseOne) == True:
    houseOneManager.checkToSweep(Sweeper, houseOne)

houseOne.printDic()

