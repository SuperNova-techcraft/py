import random
ran = int(random.randint(0, 1000))
def n():
    dij = int(input())
    if(dij < ran):
        print("the number is bigger")
        n()
    if(dij > ran):
        print("the number is littler")
        n()
    if(dij == ran):
        print("you won")
    dij = int(input())
n()