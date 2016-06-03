import math

def checkPrime(number):
    if (number == 1):
        print("Not prime")
        return
    for i in range(2, int(math.sqrt(number) + 1)):
        if (number % i == 0):
            print "Not prime"
            return
    print "Prime"
    
def Solution():
    T = int(raw_input());
    for i in range(T):
        checkPrime(int(raw_input()))
        
Solution()