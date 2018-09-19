#main controller to manage list of all spaceships and order them depending of fitness, kill 500 and generate new offspring

#create class spaceship with properties

#space/battlecontroller, check speed etc,., assing fitness level to each spaceship depending on battle
import random
import numpy

class Spaceship:
    def __init__(self, ID, race, generation, health, shields, attackSpeed, canons, premissiles, damageAmplifier, incomingDamageAmplifier, energy):
        self.ID = ID
        self.race = race
        self.generation = generation
        self.health = health
        self.shields = shields
        self.attackSpeed = attackSpeed
        self.canons = canons
        self.premissiles = premissiles
        self.damageAmplifier = damageAmplifier
        self.incomingDamageAmplifier = incomingDamageAmplifier
        self.energy = energy

    def generateOffSpring(self, ID):
        health = self.health + int(numpy.random.normal(0, 10))
        shields = self.shields + int(numpy.random.normal(0, 10))
        attackSpeed = self.attackSpeed + int(numpy.random.normal(0, 10))
        canons = self.canons + int(numpy.random.normal(0, 10))
        premissiles = self.premissiles + int(numpy.random.normal(0, 10))
        damageAmplifier = self.damageAmplifier + int(numpy.random.normal(0, 10))
        incomingDamageAmplifier = self.incomingDamageAmplifier + int(numpy.random.normal(0, 10))
        energy = self.energy + int(numpy.random.normal(0, 10))
        
        return Spaceship(ID, self.race, self.generation + 1, health, shields, attackSpeed, canons,
        premissiles, damageAmplifier, incomingDamageAmplifier, energy)

def generateSpaceShips():
    spaceshipsList = []
    for x in range(500):
        spaceshipsList.append(Spaceship(x, x, 0, int(numpy.random.normal(0, 10)), int(numpy.random.normal(0, 10)),
        int(numpy.random.normal(0, 10)), int(numpy.random.normal(0, 10)), int(numpy.random.normal(0, 10)),
        int(numpy.random.normal(0, 10)), int(numpy.random.normal(0, 10)), int(numpy.random.normal(0, 10))))
    return spaceshipsList

def battlecontroller(spaceships):
    lostSpaceShipsList = []
    
    indexes = list(range(500))
    random.shuffle(indexes)
    for x in range(250):
        index = indexes.pop()
        ss1 = spaceships[index]
        index2 = index.pop()
        ss2 = spaceships[index2]

        fightResult = fight(ss1, ss2)
        if fightResult == 0:
            print ("its a tie")
        elif fightResult < 0:
            lostSpaceShipsList.append(ss2)
        else:
            lostSpaceShipsList.append(ss1)
    return lostSpaceShipsList
    
def fight(ss1, ss2):
    return handlePremissiles(ss1, ss2)

def handlePremissiles(ss1, ss2):  
    #return -1 if player 1 wins, 0 if tie, 1 if player 2 wins  
    if ss1.premissiles > 0:
        if ss1.attackSpeed > ss2.attackSpeed:
            print ("ss1 attack ss2 with premissiles: ")
            if ss2.shields * ss2.health <= ss1.premissiles:
                return -1
    if ss2.premissiles > 0:
        print ("ss2 attack ss1 with premissiles: ")
        if ss1.shields * ss1.health <= ss2.premissiles:
            return 1
        if ss2.attackSpeed > ss1.attackSpeed:
            print ("ss1 attack ss2 with premissiles: ")
            if ss2.shields * ss2.health <= ss1.premissiles:
                return -1
    return 0
                

def main():
    ss1 = Spaceship(1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1)
    ss2 = Spaceship(1, 1, 1, 1, 1, 1 ,1, 1, 1, 1, 1)
    spaceshipsList = generateSpaceShips()
    lostSpaceshipsList = battlecontroller(spaceshipsList)
    print (spaceshipsList[0].attackSpeed)

main()