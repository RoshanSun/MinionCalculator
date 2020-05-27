import json

minionString = '''
{
  "wheat": {
    "1": {
      "actionTime": 15
    },
    "3": {
      "actionTime": 13
    },
    "5": {
      "actionTime": 11
    },
    "7": {
      "actionTime": 10
    },
    "9": {
      "actionTime": 9
    },
    "11": {
      "actionTime": 8
    }
  },
  "carrot": {
    "1": {
      "actionTime": 20
    },
    "3": {
      "actionTime": 18
    },
    "5": {
      "actionTime": 16
    },
    "7": {
      "actionTime": 14
    },
    "9": {
      "actionTime": 12
    },
    "11": {
      "actionTime": 10
    }
  },
  "potato": {
    "1": {
      "actionTime": 20
    },
    "3": {
      "actionTime": 18
    },
    "5": {
      "actionTime": 16
    },
    "7": {
      "actionTime": 14
    },
    "9": {
      "actionTime": 12
    },
    "11": {
      "actionTime": 10
    }
  },
  "pumpkin": {
    "1": {
      "actionTime": 32
    },
    "3": {
      "actionTime": 30
    },
    "5": {
      "actionTime": 27
    },
    "7": {
      "actionTime": 24
    },
    "9": {
      "actionTime": 20
    },
    "11": {
      "actionTime": 16
    }
  },
  "melon": {
    "1": {
      "actionTime": 24
    },
    "3": {
      "actionTime": 22.5
    },
    "5": {
      "actionTime": 21
    },
    "7": {
      "actionTime": 18.5
    },
    "9": {
      "actionTime": 16
    },
    "11": {
      "actionTime": 13
    }
  },
  "mushroom": {
    "1": {
      "actionTime": 30
    },
    "3": {
      "actionTime": 28
    },
    "5": {
      "actionTime": 26
    },
    "7": {
      "actionTime": 23
    },
    "9": {
      "actionTime": 20
    },
    "11": {
      "actionTime": 16
    }
  },
  "cocoabeans": {
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
      "actionTime": 15
    }
  },
  "cactus": {
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
      "actionTime": 15
    }
  },
  "sugarcane": {
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
      "actionTime": 14.5
    },
    "11": {
      "actionTime": 12
    }
  },
  "cow": {
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
  "pig": {
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
  "chicken": {
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
      "actionTime": 18
    },
    "11": {
      "actionTime": 15
    }
  },
  "sheep": {
    "1": {
      "actionTime": 24
    },
    "3": {
      "actionTime": 22
    },
    "5": {
      "actionTime": 20
    },
    "7": {
      "actionTime": 18
    },
    "9": {
      "actionTime": 16
    },
    "11": {
      "actionTime": 12
    }
  },
  "rabbit": {
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
  "netherwart": {
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
  }
}
'''

farmingMinions = json.loads(minionString)
print(farmingMinions)