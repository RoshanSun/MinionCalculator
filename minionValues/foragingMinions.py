import json

minionString = '''
{
  "oak": {
    "actionTimes": [48, 45, 42, 38, 33, 27],
    "unitPrice": 5.1
  },
  "spruce": {
    "actionTimes": [48, 45, 42, 38, 33, 27],
    "unitPrice": 5.1
  },
  "birch": {
    "actionTimes": [48, 45, 42, 38, 33, 27],
    "unitPrice": 5.7
  },
  "darkoak": {
    "actionTimes": [48, 45, 42, 38, 33, 27],
    "unitPrice": 3.3
  },
  "acacia": {
    "actionTimes": [48, 45, 42, 38, 33, 27],
    "unitPrice": 3.7
  },
  "jungle": {
    "actionTimes": [48, 45, 42, 38, 33, 27],
    "unitPrice": 5.3
  }
}
'''

treeMinions = json.loads(minionString)