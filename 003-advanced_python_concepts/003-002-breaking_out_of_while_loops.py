# https://stackskills.com/courses/102831/lectures/1499469

import random

playerhp = 260
enemyatkl = 60
enemyatkh = 80

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 0:
        playerhp = 0
    
    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

    if playerhp == 0:
        print("You have died.\n")

playerhp = 260

while playerhp > 0:
    dmg = random.randrange(enemyatkl, enemyatkh)
    playerhp = playerhp - dmg

    if playerhp <= 30:
        playerhp = 30

    print("Enemy strikes for", dmg, "points of damage. Current HP is", playerhp)

    if playerhp == 30:
        print("You have low health, you've been transported to the nearest inn.")
        break
