def collatz(number):
    if number % 2 == 0:
        print(number//2)
        return(number // 2)
    if number % 2 != 0:
        print(3*number+1)
        return(3*number+1)
    
new = input("What number? ")
try: 
    new = int(new)
    while new != 1:
        new = collatz(new)
except ValueError:
    print("Error, invalid argument")