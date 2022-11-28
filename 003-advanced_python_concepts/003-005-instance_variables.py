# https://stackskills.com/courses/102831/lectures/1499472

class Enemy:
    
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh


    def getAtk(self):
        print("Low Attack is", self.atkl)

enemy1 = Enemy(40, 49)
enemy1.getAtk()

enemy2 = Enemy(75, 90)
enemy2.getAtk()
