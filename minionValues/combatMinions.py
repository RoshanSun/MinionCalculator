import json

minionString = '''
{
  "zombie": {
    "actionTimes": [26, 24, 22, 20, 17, 13],
    "unitPrice": 9
  },
  "skeleton": {
    "actionTimes": [26, 24, 22, 20, 17, 13],
    "unitPrice": 9.6
  },
  "spider": {
    "actionTimes": [26, 24, 22, 20, 17, 13],
    "stringPrice": 5.9,
    "eyePrice": 10.5
  },
  "cavespider": {
    "actionTimes": [26, 24, 22, 20, 17, 13],
    "stringPrice": 5.9,
    "eyePrice": 10.5
  },
  "creeper": {
    "actionTimes": [27, 25, 23, 21, 18, 14],
    "unitPrice": 12.1
  },
  "enderman": {
    "actionTimes": [32, 30, 28, 25, 22, 18],
    "unitPrice": 7.7
  },
  "ghast": {
    "actionTimes": [50, 47, 44, 41, 38, 32],
    "unitPrice": 18.3
  },
  "slime": {
    "actionTimes": [26, 24, 22, 19, 16, 12],
    "unitPrice": 6.2
  },
  "blaze": {
    "actionTimes": [33, 31, 28.5, 25, 21, 16.5],
    "unitPrice": 22.1
  },
  "magmacube": {
    "actionTimes": [32, 30, 28, 25, 22, 18],
    "unitPrice": 6.2
  }
}
'''

combatMinions = json.loads(minionString)