import json

minionString = '''
{
  "zombie": {
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
      "actionTime": 20
    },
    "9": {
      "actionTime": 17
    },
    "11": {
      "actionTime": 13
    }
  },
  "skeleton": {
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
      "actionTime": 20
    },
    "9": {
      "actionTime": 17
    },
    "11": {
      "actionTime": 13
    }
  },
  "spider": {
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
      "actionTime": 20
    },
    "9": {
      "actionTime": 17
    },
    "11": {
      "actionTime": 13
    }
  },
  "cavespider": {
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
      "actionTime": 20
    },
    "9": {
      "actionTime": 17
    },
    "11": {
      "actionTime": 13
    }
  },
  "creeper": {
    "1": {
      "actionTime": 27
    },
    "3": {
      "actionTime": 25
    },
    "5": {
      "actionTime": 23
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
  "enderman": {
    "1": {
      "actionTime": 32
    },
    "3": {
      "actionTime": 30
    },
    "5": {
      "actionTime": 28
    },
    "7": {
      "actionTime": 25
    },
    "9": {
      "actionTime": 22
    },
    "11": {
      "actionTime": 18
    }
  },
  "ghast": {
    "1": {
      "actionTime": 50
    },
    "3": {
      "actionTime": 47
    },
    "5": {
      "actionTime": 44
    },
    "7": {
      "actionTime": 41
    },
    "9": {
      "actionTime": 38
    },
    "11": {
      "actionTime": 32
    }
  },
  "slime": {
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
      "actionTime": 12
    }
  },
  "blaze": {
    "1": {
      "actionTime": 33
    },
    "3": {
      "actionTime": 31
    },
    "5": {
      "actionTime": 28.5
    },
    "7": {
      "actionTime": 25
    },
    "9": {
      "actionTime": 21
    },
    "11": {
      "actionTime": 16.5
    }
  },
  "magmacube": {
    "1": {
      "actionTime": 32
    },
    "3": {
      "actionTime": 30
    },
    "5": {
      "actionTime": 28
    },
    "7": {
      "actionTime": 25
    },
    "9": {
      "actionTime": 22
    },
    "11": {
      "actionTime": 18
    }
  }
}
'''

combatMinions = json.loads(minionString)
print(combatMinions)