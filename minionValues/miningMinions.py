import json

minionString = '''
{
  "cobble": {
    "actionTimes": [14, 12, 10, 9, 8, 7],
    "unitPrice": 5
  },
  "coal": {
    "actionTimes": [15, 13, 12, 10, 9, 7],
    "unitPrice": 10.6
  },
  "iron": {
    "actionTimes": [17, 15, 14, 12, 10, 8],
    "unitPrice": 5.6
  },
  "gold": {
    "actionTimes": [22, 20, 18, 16, 14, 11],
    "unitPrice": 11
  },
  "diamond": {
    "actionTimes": [29, 27, 25, 22, 19, 15],
    "unitPrice": 7.3
  },
  "lapis": {
    "actionTimes": [29, 27, 25, 23, 21, 18],
    "unitPrice": 3.3
  },
  "emerald": {
    "actionTimes": [28, 26, 24, 21, 18, 14],
    "unitPrice": 6
  },
  "redstone": {
    "actionTimes": [29, 27, 25, 23, 21, 18],
    "unitPrice": 2.4
  },
  "quartz": {
    "actionTimes": [22.5, 21, 19, 17, 14.5, 11.5],
    "unitPrice": 19.3
  },
  "obsidian": {
    "actionTimes": [45, 42, 39, 35, 30, 24],
    "unitPrice": 23.7
  },
  "glowstone": {
    "actionTimes": [25, 23, 21, 19, 16, 13],
    "unitPrice": 13.8
  },
  "gravel": {
    "actionTimes": [26, 24, 22, 19, 16, 13],
    "unitPrice": 2.2,
    "flintPrice": 16.5
  },
  "ice": {
    "actionTimes": [14, 12, 10, 9, 8, 7],
    "unitPrice": 3.1
  },
  "sand": {
    "actionTimes": [26, 24, 22, 19, 16, 13],
    "unitPrice": 9.5
  },
  "endstone": {
    "actionTimes": [26, 24, 22, 19, 16, 13],
    "unitPrice": 14.9
  },
  "snow": {
    "actionTimes": "not sure, will fill this in ASAP",
    "unitPrice": 1.1
  }
}
'''

miningMinions = json.loads(minionString)