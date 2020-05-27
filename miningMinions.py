import json

minionString = '''
{
  "cobble": {
    "1": {
      "actionTime": 14
    },
    "3": {
      "actionTime": 12
    },
    "5": {
      "actionTime": 10
    },
    "7": {
      "actionTime": 9
    },
    "9": {
      "actionTime": 8
    },
    "11": {
      "actionTime": 7
    }
  },
  "coal": {
    "1": {
      "actionTime": 15
    },
    "3": {
      "actionTime": 13
    },
    "5": {
      "actionTime": 12
    },
    "7": {
      "actionTime": 10
    },
    "9": {
      "actionTime": 9
    },
    "11": {
      "actionTime": 7
    }
  },
  "iron": {
    "1": {
      "actionTime": 17
    },
    "3": {
      "actionTime": 15
    },
    "5": {
      "actionTime": 14
    },
    "7": {
      "actionTime": 12
    },
    "9": {
      "actionTime": 10
    },
    "11": {
      "actionTime": 8
    }
  },
  "gold": {
    "1": {
      "actionTime": 22
    },
    "3": {
      "actionTime": 20
    },
    "5": {
      "actionTime": 18
    },
    "7": {
      "actionTime": 16
    },
    "9": {
      "actionTime": 14
    },
    "11": {
      "actionTime": 11
    }
  },
  "diamond": {
    "1": {
      "actionTime": 29
    },
    "3": {
      "actionTime": 27
    },
    "5": {
      "actionTime": 25
    },
    "7": {
      "actionTime": 22
    },
    "9": {
      "actionTime": 19
    },
    "11": {
      "actionTime": 15
    }
  },
  "lapis": {
    "1": {
      "actionTime": 29
    },
    "3": {
      "actionTime": 27
    },
    "5": {
      "actionTime": 25
    },
    "7": {
      "actionTime": 23
    },
    "9": {
      "actionTime": 21
    },
    "11": {
      "actionTime": 18
    }
  },
  "emerald": {
    "1": {
      "actionTime": 28
    },
    "3": {
      "actionTime": 26
    },
    "5": {
      "actionTime": 24
    },
    "7": {
      "actionTime": 21
    },
    "9": {
      "actionTime": 18
    },
    "11": {
      "actionTime": 14
    }
  },
  "redstone": {
    "1": {
      "actionTime": 29
    },
    "3": {
      "actionTime": 27
    },
    "5": {
      "actionTime": 25
    },
    "7": {
      "actionTime": 23
    },
    "9": {
      "actionTime": 21
    },
    "11": {
      "actionTime": 18
    }
  },
  "quartz": {
    "1": {
      "actionTime": 22.5
    },
    "3": {
      "actionTime": 21
    },
    "5": {
      "actionTime": 19
    },
    "7": {
      "actionTime": 17
    },
    "9": {
      "actionTime": 14.5
    },
    "11": {
      "actionTime": 11.5
    }
  },
  "obsidian": {
    "1": {
      "actionTime": 45
    },
    "3": {
      "actionTime": 42
    },
    "5": {
      "actionTime": 39
    },
    "7": {
      "actionTime": 35
    },
    "9": {
      "actionTime": 30
    },
    "11": {
      "actionTime": 24
    }
  },
  "glowstone": {
    "1": {
      "actionTime": 25
    },
    "3": {
      "actionTime": 23
    },
    "5": {
      "actionTime": 21
    },
    "7": {
      "actionTime": 19
    },
    "9": {
      "actionTime": 16
    },
    "11": {
      "actionTime": 13
    }
  },
  "gravel": {
    "1": {
      "actionTime": 26
    },
    "3": {
      "actionTime": 24
    },
    "5": {
      "actionTime": 22
    },
    "7": {
      "actionTime": 19
    },
    "9": {
      "actionTime": 16
    },
    "11": {
      "actionTime": 13
    }
  },
  "ice": {
    "1": {
      "actionTime": 14
    },
    "3": {
      "actionTime": 12
    },
    "5": {
      "actionTime": 10
    },
    "7": {
      "actionTime": 9
    },
    "9": {
      "actionTime": 8
    },
    "11": {
      "actionTime": 7
    }
  },
  "sand": {
    "1": {
      "actionTime": 26
    },
    "3": {
      "actionTime": 24
    },
    "5": {
      "actionTime": 22
    },
    "7": {
      "actionTime": 19
    },
    "9": {
      "actionTime": 16
    },
    "11": {
      "actionTime": 13
    }
  },
  "endstone": {
    "1": {
      "actionTime": 26
    },
    "3": {
      "actionTime": 24
    },
    "5": {
      "actionTime": 22
    },
    "7": {
      "actionTime": 19
    },
    "9": {
      "actionTime": 16
    },
    "11": {
      "actionTime": 13
    }
  }
}
'''

miningMinions = json.loads(minionString)
print(miningMinions)