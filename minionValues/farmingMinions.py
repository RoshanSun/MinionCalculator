import json

minionString = '''
{
  "wheat": {
    "actionTimes": [15, 13, 11, 10, 9, 8],
    "unitPrice": 3.6,
    "itemsPer": 0.5
  },
  "carrot": {
    "actionTimes": [20, 18, 16, 14, 12, 10],
    "unitPrice": 5.6,
    "itemsPer": 1.5
  },
  "potato": {
    "actionTimes": [15, 13, 11, 10, 9, 8],
    "unitPrice": 3.6,
    "itemsPer": 1.5
  },
  "pumpkin": {
    "actionTimes": [32, 30, 27, 24, 20, 16],
    "unitPrice": 3.2,
    "itemsPer": 1
  },
  "melon": {
    "actionTimes": [24, 22.5, 21, 18.5, 16, 13],
    "unitPrice": 2.7,
    "itemsPer": 5
  },
  "mushroom": {
    "actionTimes": [30, 28, 26, 23, 20, 16],
    "unitPrice": 13.3,
    "itemsPer": 0.5
  },
  "cocoabeans": {
    "actionTimes": [27, 25, 23, 21, 18, 15],
    "unitPrice": 4.4,
    "itemsPer": 1.5
  },
  "cactus": {
    "actionTimes": [27, 25, 23, 21, 18, 15],
    "unitPrice": 4.5,
    "itemsPer": 1.5
  },
  "sugarcane": {
    "actionTimes": [22, 20, 18, 16, 14.5, 12],
    "unitPrice": 5.6,
    "itemsPer": 1.5
  },
  "cow": {
    "actionTimes": [26, 24, 22, 20, 17, 13],
    "unitPrice": 16.2,
    "itemsPer": 0.5
  },
  "pig": {
    "actionTimes": [26, 24, 22, 20, 17, 13],
    "unitPrice": 10.8,
    "itemsPer": 0.5
  },
  "chicken": {
    "actionTimes": [26, 24, 22, 20, 18, 15],
    "unitPrice": 9,
    "itemsPer": 0.5
  },
  "sheep": {
    "actionTimes": [24, 22, 20, 18, 16, 12],
    "unitPrice": 21.1,
    "itemsPer": 0.5
  },
  "rabbit": {
    "actionTimes": [26, 24, 22, 20, 17, 13],
    "unitPrice": 13.4,
    "itemsPer": 0.5
  },
  "netherwart": {
    "actionTimes": [50, 47, 44, 41, 38, 32],
    "unitPrice": 8.6,
    "itemsPer": 1.25 
  }
}
'''

farmingMinions = json.loads(minionString)