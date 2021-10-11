import time

def clear():
    print("\n"*45)

print("Welcome to Pythonmon!")

user = input("Press enter to start.")

enimyHp = 100
playerHp = 100
superPunch = 0 

while True:
    
    clear()
    
    
    print("                      _______                    ")
    print("                     |       |            /\\    ")
    print("                     |       |           /  \\   ")
    print("                     |       |          /    \\  ")
    print("                     |_______|         /______\\ ")
    print("\n                      HP: " + str(playerHp) + "         HP: " + str(enimyHp))
    print("\n ____________________________________________________________________")
    print("| Choose your atack:                                                 |")
    print("|                                                                    |")
    print("| A) Punch [10]                                                      |")
    print("| B) Kick [15]                                                       |")
    print("| C) SuperPunch [30] (3 Rounds)                                      |")
    print("|____________________________________________________________________|")
    
    while True:
        user = input()
        if user == "a":
    
            enimyHp -= 10
    
            superPunch += 1
            
            clear()
    
            print("                      _______                    ")
            print("                     |       |            /\\    ")
            print("                     |       |           /  \\   ")
            print("                     |       |          /    \\  ")
            print("                     |_______|         /______\\ ")
            print("\n                      HP: " + str(playerHp) + "         HP: " + str(enimyHp))
            print("\n ____________________________________________________________________")
            print("| You choosed Punch!                                                 |")
            print("|                                                                    |")
            print("|                                                                    |")
            print("|                                                                    |")
            print("|                                                                    |")
            print("|____________________________________________________________________|")
    
            if enimyHp <= 0:
                enimyHp = 0
                break
            else:
                break
    
        if user == "b":
    
            enimyHp -= 15
    
            superPunch += 1
            
            clear()
    
            print("                      _______                    ")
            print("                     |       |            /\\    ")
            print("                     |       |           /  \\   ")
            print("                     |       |          /    \\  ")
            print("                     |_______|         /______\\ ")
            print("\n                      HP: " + str(playerHp) + "         HP: " + str(enimyHp))
            print("\n ____________________________________________________________________")
            print("| You choosed Kick!                                                  |")
            print("|                                                                    |")
            print("|                                                                    |")
            print("|                                                                    |")
            print("|                                                                    |")
            print("|____________________________________________________________________|")
    
            if enimyHp <= 0:
                enimyHp = 0
                break
            else:
                break
    
        if user == "c" and superPunch >= 3:
    
            enimyHp -= 30
    
            superPunch = 0
            
            clear()
    
            print("                      _______                    ")
            print("                     |       |            /\\    ")
            print("                     |       |           /  \\   ")
            print("                     |       |          /    \\  ")
            print("                     |_______|         /______\\ ")
            print("\n                      HP: " + str(playerHp) + "         HP: " + str(enimyHp))
            print("\n ____________________________________________________________________")
            print("| You choosed SuperPunch!                                            |")
            print("|                                                                    |")
            print("|                                                                    |")
            print("|                                                                    |")
            print("|                                                                    |")
            print("|____________________________________________________________________|")

            if enimyHp <= 0:
                enimyHp = 0
                break
            else:
                break

    if enimyHp <= 0:
        
        clear()
    
        print("                      _______                    ")
        print("                     |       |            /\\    ")
        print("                     |       |           /  \\   ")
        print("                     |       |          /    \\  ")
        print("                     |_______|         /______\\ ")
        print("\n                      HP: " + str(playerHp) + "         HP: " + str(enimyHp))
        print("\n ____________________________________________________________________")
        print("| You win!                                                           |")
        print("|                                                                    |")
        print("|                                                                    |")
        print("|                                                                    |")
        print("|                                                                    |")
        print("|____________________________________________________________________|")
        
        break
    
    user = input()

    playerHp -= 15
    
            
    clear()
    
    print("                      _______                    ")
    print("                     |       |            /\\    ")
    print("                     |       |           /  \\   ")
    print("                     |       |          /    \\  ")
    print("                     |_______|         /______\\ ")
    print("\n                      HP: " + str(playerHp) + "         HP: " + str(enimyHp))
    print("\n ____________________________________________________________________")
    print("| Enimy choosed Kick!                                                |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|                                                                    |")
    print("|____________________________________________________________________|")

    user = input()

    if playerHp <= 0:
        
        playerHp = 0
        
        clear()
    
        print("                      _______                    ")
        print("                     |       |            /\\    ")
        print("                     |       |           /  \\   ")
        print("                     |       |          /    \\  ")
        print("                     |_______|         /______\\ ")
        print("\n                      HP: " + str(playerHp) + "         HP: " + str(enimyHp))
        print("\n ____________________________________________________________________")
        print("| You Lost!                                                          |")
        print("|                                                                    |")
        print("|                                                                    |")
        print("|                                                                    |")
        print("|                                                                    |")
        print("|____________________________________________________________________|")
        
        break

    
    
