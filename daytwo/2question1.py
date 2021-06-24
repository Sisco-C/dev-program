def isintPowerOfFour(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 4 != 0):
                return False
            n = n // 4
             
    return True
 
trial_int = 100
if(isintPowerOfFour(100)):
    print(trial_int, 'is a power of 4')
else:
    print(trial_int, 'is not a power of 4')
 