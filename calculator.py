#Comment to track changes
def add (a,b):
    return a+b
def subtract (a,b):
    return a-b
def multiply (a,b):
    return a*b
def divide (a,b):
    if b==0:
        return "Error: Cannot divide by zero"
    return a/b
# Simple demonstration
if __name__ == "__main__":
    print ("Calculator Demo:")
    print ("2 + 3 =",add(2,3))
    print ("10 - 4 =",subtract(10,4))
    print ("5 * 6 =",multiply(5,6))
    print ("15 / 3 =",divide(15,3))
    print ("10 / 0 =",divide(10,0))
    