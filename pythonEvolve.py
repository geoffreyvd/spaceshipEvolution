#main controller to manage list of all spaceships and order them depending of fitness, kill 500 and generate new offspring

#create class spaceship with properties

#space/battlecontroller, check speed etc,., assing fitness level to each spaceship depending on battle
import random
import numpy

globVarSpaceshipIndex = 0

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
        damageAmplifier = self.damageAmplifier + int(numpy.random.normal(0, 2))
        incomingDamageAmplifier = self.incomingDamageAmplifier + int(numpy.random.normal(0, 2))
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
        int(numpy.random.normal(0, 2)), int(numpy.random.normal(0, 2)), int(numpy.random.normal(0, 10))))
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

        global globVarSpaceshipIndex
        globVarSpaceshipIndex = x

        if globVarSpaceshipIndex == 1:
            print(str(ss1))
            print(" VS ")
            print(str(ss2))
        fightResult = fight(ss1, ss2)

        if fightResult == 0:
            if globVarSpaceshipIndex == 1:
                print ("its a tie")
            #print("tie: " + str(ss1) + " -VS- " + str(ss2))
            lostSpaceshipsList.append(index1)
            lostSpaceshipsList.append(index2)
        elif fightResult < 0:
            lostSpaceshipsList.append(index2)
            aliveSpaceshipsList.append(index1)
            if globVarSpaceshipIndex == 1:
                print ("player 1 wins")
        else:
            lostSpaceshipsList.append(index1)
            aliveSpaceshipsList.append(index2)
            if globVarSpaceshipIndex == 1:
                print ("player 2 wins")
    return (lostSpaceshipsList, aliveSpaceshipsList)
    
def fight(ss1, ss2):
    check = preFightCheck(ss1, ss2)
    if check != 2:
        return check
    premissilesFight = handlePremissiles(ss1, ss2)
    if premissilesFight != 0: #0 is a tie, which is fine for premissiles fight
        return premissilesFight
    return handleCombat(ss1, ss2)

def preFightCheck(ss1, ss2):
    #return -1 if player 1 wins, 0 if tie, 1 if player 2 wins 
    energy1 = checkEnergy(ss1)
    energy2 = checkEnergy(ss2)

    if globVarSpaceshipIndex == 1:
        print ("energy1: " + str(energy1))
        print ("energy2: " + str(energy2))

    if ss1.shields <= 0 or ss1.health <= 0 or ss1.damageAmplifier <= 0 or energy1 <= 0:
        if ss2.shields <= 0 or ss2.health <= 0 or ss2.damageAmplifier <= 0 or energy2 <= 0:
            if globVarSpaceshipIndex == 1:
                print ("both spaceships do not have what it takes to fight")
            return 0
        if globVarSpaceshipIndex == 1:
            print ("spaceship 1 do not have what it takes to fight")
        return 1
    if ss2.shields <= 0 or ss2.health <= 0  or ss2.damageAmplifier <= 0 or energy2 <= 0:
        if globVarSpaceshipIndex == 1:
            print ("spaceship 2 do not have what it takes to fight")
        return -1
    return 2

    
def checkEnergy(ss):
    energy = ss.energy + 10
    if energy < 0 or energy > 300:
        return -1

    #game balance options
    energy -= assignWeightToProperty(ss.health, 1.25)
    energy -= assignWeightToProperty(ss.shields, 1.25)
    energy -= assignWeightToProperty(ss.attackSpeed, 1.05)
    energy -= assignWeightToProperty(ss.canons, 1.1)
    energy -= assignWeightToProperty(ss.premissiles, 0.8)
    energy -= assignWeightToProperty(ss.damageAmplifier, 1.4)
    energy -= assignWeightToProperty(ss.incomingDamageAmplifier, 1.2)
    return energy

def assignWeightToProperty(propertyValue, weight):
    if propertyValue <= 0:
        return 0
    else:
        return int(numpy.power(propertyValue, weight))

def handlePremissiles(ss1, ss2):  
    #return -1 if player 1 wins, 0 if tie, 1 if player 2 wins  
    ss2IncomingDmgAmp = 0
    if ss2.incomingDamageAmplifier > 0:
        ss2IncomingDmgAmp = ss2.incomingDamageAmplifier
    ss1IncomingDmgAmp = 0
    if ss1.incomingDamageAmplifier > 0:
        ss1IncomingDmgAmp = ss1.incomingDamageAmplifier

    ss1DmgAmp = ss1.damageAmplifier - ss2IncomingDmgAmp
    if ss1DmgAmp < 1:
        ss1DmgAmp = 1
    ss2DmgAmp = ss2.damageAmplifier - ss1IncomingDmgAmp
    if ss2DmgAmp < 1:
        ss2DmgAmp = 1


    if ss1.premissiles > 0:
        if ss2.premissiles > 0:
            if ss1.attackSpeed > ss2.attackSpeed:
                #print ("ss1 attack ss2 with premissiles: ")
                if ss2.shields * ss2.health <= ss1.premissiles * ss1DmgAmp:
                    if globVarSpaceshipIndex == 1:
                        print ("spaceship 2 got killed by premissile")
                    return -1
            else:
                #print ("ss2 attack ss1 with premissiles: ")
                if ss1.shields * ss1.health <= ss2.premissiles * ss2DmgAmp:
                    if globVarSpaceshipIndex == 1:
                        print ("spaceship 1 got killed by premissile")
                    return 1
        else:
            if ss2.shields * ss2.health <= ss1.premissiles * ss1DmgAmp:
                if globVarSpaceshipIndex == 1:
                    print ("spaceship 2 got killed by premissile")
                return -1
    if ss2.premissiles > 0:
        #print ("ss2 attack ss1 with premissiles: ")
        if ss1.shields * ss1.health <= ss2.premissiles * ss2DmgAmp:
            if globVarSpaceshipIndex == 1:
                print ("spaceship 1 got killed by premissile")
            return 1
    if globVarSpaceshipIndex == 1:
        print ("somehow none got killed by premissiles")
    return 0

def handleCombat(ss1, ss2):
    #return -1 if player 1 wins, 0 if tie, 1 if player 2 wins 
    ss2IncomingDmgAmp = 0
    if ss2.incomingDamageAmplifier > 0:
        ss2IncomingDmgAmp = ss2.incomingDamageAmplifier
    ss1IncomingDmgAmp = 0
    if ss1.incomingDamageAmplifier > 0:
        ss1IncomingDmgAmp = ss1.incomingDamageAmplifier

    health1 = ss1.shields * ss1.health
    health2 = ss2.shields * ss2.health
    if ss1.attackSpeed > ss2.attackSpeed:
        health2 -= (ss1.canons * (ss1.damageAmplifier - ss2IncomingDmgAmp))
        if globVarSpaceshipIndex == 1:
            print ("remaining health of ss2: " + str(health2))
        if health2 < 0:
            return -1
            
    for x in range(10):
        health1 -= (ss2.canons * (ss2.damageAmplifier - ss1IncomingDmgAmp))
        if globVarSpaceshipIndex == 1:
            print("remaining health of ss1: " + str(health1))
        if health1 < 0:
            return 1
        health2 -= (ss1.canons * (ss1.damageAmplifier - ss2IncomingDmgAmp))
        if globVarSpaceshipIndex == 1:
            print ("remaining health of ss2: " + str(health2))
        if health2 < 0:
            return -1
    #print("this shouldnt happen")
    #todo fix this 0
    return 0
        

def main():
    idIncrement = 501
    spaceshipsList = generateSpaceShips()
    for x in range(500):
        lostSpaceshipsList, remainingIndexes = battlecontroller(spaceshipsList)
        for x in range(len(lostSpaceshipsList)):
            deadIndex = lostSpaceshipsList[x]
            spaceshipsList[deadIndex] = spaceshipsList[remainingIndexes[x % len(remainingIndexes)]].generateOffSpring(idIncrement+1)

    for x in range(len(spaceshipsList)):
        print(spaceshipsList[x])

    strongestSpaceShip = spaceshipsList[0]
    for x in range(len(spaceshipsList)):        
        if fight(strongestSpaceShip, spaceshipsList[x]) == 1:
            strongestSpaceShip = spaceshipsList[x]
    print("strongest spaceship: " + str(strongestSpaceShip))
main()