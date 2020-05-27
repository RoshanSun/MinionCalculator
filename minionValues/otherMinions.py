import json

minionString = '''
{
  "fish": {
    "actionTimes": [78, 75, 72, 68, 62.5, 53, 35],
    "fishPrice": 26.6,
    "salmonPrice": 8.6,
    "clownPrice": 17.7,
    "pufferPrice": 12.1,
    "shardPrice": 3.9,
    "crystalsPrice": 4.5,
    "inkPrice": 235.8,
    "spongePrice": 168.7
  },
  "clay": {
    "actionTimes": [32, 30, 27.5, 24, 20, 16],
    "unitPrice": 5.2
  },
  "revenant": {
    "actionTimes": [],
    "unitPrice": 0
  },
  "tarantula": {
    "actionTimes": [],
    "unitPrice": 0
  },
  "flower": {
    "actionTimes": [],
    "unitPrice": 0
  }
}
'''

otherMinions = json.loads(minionString)