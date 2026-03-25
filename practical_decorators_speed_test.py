# ----------------------------------------
# -- decorators => practical speed test --
# ----------------------------------------

from time import time


def speedtest(func):
    
    def wrapper():
        
        start = time()
        
        func()
        
        end = time()
        
        print(f"function running time is: {end - start}")
        
    return wrapper

@speedtest
def bigloop() :
    
    for number in range(1, 20000) :
        
        print(number)
        
bigloop()        