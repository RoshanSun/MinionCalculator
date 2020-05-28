from minionValues.farmingMinions import farmingMinions as fm
from minionValues.miningMinions import miningMinions as mm
from minionValues.combatMinions import combatMinions as cm
from minionValues.foragingMinions import treeMinions as tm
from minionValues.otherMinions import otherMinions as om
import json

#print(fm)
#print(mm)
#print(cm)
#print(tm)
#print(om)

allMinions = dict()
allMinions["farming"] = fm
allMinions["mining"] = mm
allMinions["combat"] = cm
allMinions["tree"] = tm
allMinions["other"] = om

counter = 1
print("From the following, choose the category of minions you're using:")
for keys in allMinions:
  print(f'{counter}. {keys}')
  counter += 1
category = input("Make your pick: ")

chosenSet = allMinions[category]

counter = 1
print("Which type of minion will you use?:")
for keys in chosenSet:
  print(f'{counter}. {keys}')
  counter += 1
minion = input("Make your pick: ")
chosen = chosenSet[minion]
tier = input("What tier of this minion?: ")
tier = int(tier)
quantity = input("How many of these minions are you using?: ")

actionTime = chosen["actionTimes"][(tier-1)//2]
unitPrice = chosen["unitPrice"]
numItems = chosen["itemsPer"]
hourlyEarnings = 86400/actionTime * unitPrice * numItems
print(f'Each minion makes {} coins each hour => all {quantity} minions make {} each hour.')

# value = input("Please enter a bopbop:\n")
# print(value)

# Earnings = 86,400 / Action Time * Items Per Action * Unit Price + 138,240 / Action Time
# Bonus Speed = Base Speed * (1 - (speed bonus sum / (1 + speed bonus sum)))