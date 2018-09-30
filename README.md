# spaceshipEvolution
Spaceship arena evolution, 

The spaceships get randomly choosen to fight another spaceship, the survivor will survive (duh) and generate offspring with mutations. The mutations aren't just random, they are normally distributed, which I thought would be quite interesting because it closer immitates nature.
The spaceships have properties such as health, shields, attackspeeds, cannons and energy. mutations are done on these properties.
The fights basically look like this:
1) does the space even have enough energy to power its components (propertys), the energy consumption is calculated in the checkEnergy function, and is determined per property. This is also the most interesting part of the evolve application, because tweaking those numbers will result in very different resulst.
2) premissiles, does the spaceship have premissiles? These can be fired once. Lets the one with highest attack speed fire first. If no one dies continue to combat phase
3) combat phase: spacehsip 1 dmg = canons * (ss1.dmgAmp - ss2.incomingDmgAmp)
                 spaceship 2 life = health * shields
                 then for every round inflict dmg on life
                 see who kills the other one in 5 rounds,
4) none died? both lose!

So it begins with 1000 species and will result in some species dominating and countering each other.
