import random

def rnd_game():
    inputTimes = 1
    val = random.randint(0,100)
    inputVal = inputValidNumber()
    while val != inputVal:
        if inputVal > val:
            print(" > ?")
        if inputVal < val:
            print(" < ?")
        inputVal = inputValidNumber() 
        inputTimes += 1
    print("number is:",val)
    print("input times:",inputTimes)


def inputValidNumber() -> int :
    a = input("input a number:")
    while True:
        try:
            return int(a)
        except:
            print("input number wrong!")
            a = input("input a number:")

rnd_game()
    
