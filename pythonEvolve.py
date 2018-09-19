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
    def __str__(self):
        return ("race: " + str(self.race) + ", generation: " + str(self.generation) + ", hp: " + str(self.health) + ", shields: " + str(self.shields) + ", as: " + str(self.attackSpeed) +
        ", canons: " + str(self.canons) + ", premissiles: " + str(self.premissiles) + ", dmgAmp: " + str(self.damageAmplifier)
        + ", incDmgAmp: " + str(self.incomingDamageAmplifier) + ", energy" + str(self.energy)) 

def generateSpaceShips():
    spaceshipsList = []
    for x in range(500):
        spaceshipsList.append(Spaceship(x, x, 0, int(numpy.random.normal(0, 10)), int(numpy.random.normal(0, 10)),
        int(numpy.random.normal(0, 10)), int(numpy.random.normal(0, 10)), int(numpy.random.normal(0, 10)),
        int(numpy.random.normal(0, 10)), int(numpy.random.normal(0, 10)), int(numpy.random.normal(0, 10))))
    return spaceshipsList

def battlecontroller(spaceships):
    lostSpaceshipsList = []
    aliveSpaceshipsList = []
    indexes = list(range(500))
    random.shuffle(indexes)
    for x in range(250):
        index1 = indexes.pop()
        ss1 = spaceships[index1]
        index2 = indexes.pop()
        ss2 = spaceships[index2]

        #print(str(ss1) + " VS " + str(ss2))
        fightResult = fight(ss1, ss2)
        if fightResult == 0:
            #print ("its a tie")
            print("tie: " + str(ss1) + " -VS- " + str(ss2))
            lostSpaceshipsList.append(index1)
            lostSpaceshipsList.append(index2)
        elif fightResult < 0:
            lostSpaceshipsList.append(index1)
            aliveSpaceshipsList.append(index2)
            #print ("player 1 wins")
        else:
            lostSpaceshipsList.append(index2)
            aliveSpaceshipsList.append(index1)
            #print ("player 2 wins")
    return (lostSpaceshipsList, aliveSpaceshipsList)
    
def fight(ss1, ss2):
    check = preFightCheck(ss1, ss2)
    if check != 2:
        return check
    premissilesFight = handlePremissiles(ss1, ss2)
    if premissilesFight != 0:
        return premissilesFight
    return handleCombat(ss1, ss2)

def preFightCheck(ss1, ss2):
    #return -1 if player 1 wins, 0 if tie, 1 if player 2 wins 
    if ss1.shields | ss1.health <= 0:
        if ss2.shields | ss2.health <= 0:
            return 0
        return 1
    if ss2.shields | ss2.health <= 0:
        return -1
    return 2

def handlePremissiles(ss1, ss2):  
    #return -1 if player 1 wins, 0 if tie, 1 if player 2 wins  
    if ss1.premissiles > 0:
        if ss1.attackSpeed > ss2.attackSpeed:
            #print ("ss1 attack ss2 with premissiles: ")
            if ss2.shields * ss2.health <= ss1.premissiles:
                return -1
    if ss2.premissiles > 0:
        #print ("ss2 attack ss1 with premissiles: ")
        if ss1.shields * ss1.health <= ss2.premissiles:
            return 1
        if ss2.attackSpeed > ss1.attackSpeed:
            #print ("ss1 attack ss2 with premissiles: ")
            if ss2.shields * ss2.health <= ss1.premissiles:
                return -1
    return 0

def handleCombat(ss1, ss2):
    #return -1 if player 1 wins, 0 if tie, 1 if player 2 wins 
    if ss1.attackSpeed > ss2.attackSpeed:
        health2 = ss2.shields * ss2.health - (ss1.canons * (ss1.damageAmplifier - ss2.incomingDamageAmplifier + 1))
        if health2 < 0:
            return -1
    while True:
        health1 = ss1.shields * ss1.health - (ss2.canons * (ss2.damageAmplifier - ss1.incomingDamageAmplifier + 1))
        if health1 < 0:
            return 1
        health2 = ss2.shields * ss2.health - (ss1.canons * (ss1.damageAmplifier - ss2.incomingDamageAmplifier + 1))
        if health2 < 0:
            return -1
    print("this shouldnt happen")
    return 0
        

def main():
    idIncrement = 501
    spaceshipsList = generateSpaceShips()
    for x in range(10000):
        lostSpaceshipsList, remainingIndexes = battlecontroller(spaceshipsList)
        for x in range(len(lostSpaceshipsList)):
            deadIndex = lostSpaceshipsList[x]
            spaceshipsList[deadIndex] = spaceshipsList[remainingIndexes[x % len(remainingIndexes)]].generateOffSpring(idIncrement+1)

    for x in range(len(spaceshipsList)):
        print(spaceshipsList[x])
main()