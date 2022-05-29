import random
response= str(y)
while response== y:
    no = random.randint(1,6)

    if (no == 1):
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        print("Press y to roll again and n to exit: ",response)
    elif(no == 2):
        print("[-----]")
        print("[     ]")
        print("[0   0]")
        print("[     ]")
        print("[-----]")
        print("Press y to roll again and n to exit: ",response)
    elif(no == 3):
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        print("Press y to roll again and n to exit: ",response)
    elif(no == 4):
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        print("Press y to roll again and n to exit: ",response)
    elif(no == 5):
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        print("Press y to roll again and n to exit: ",response)
    elif(no == 6):
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
        print("Press y to roll again and n to exit: ",response)
