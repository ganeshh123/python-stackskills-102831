# https://stackskills.com/courses/102831/lectures/1499471

class Enemy:
    atkl = 60
    atkh = 80

    def getAtk(self):
        print("Low Attack is", self.atkl)

enemy1 = Enemy()
enemy1.getAtk()

enemy2 = Enemy()
enemy2.getAtk()
