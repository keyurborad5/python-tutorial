import math

def pi():
    """Returns the value of pi."""
    return math.pi
def square_root(x):
    """Returns the square root of x."""
    return math.sqrt(x)

def power(x, y):
    """Returns x raised to the power of y."""
    return math.pow(x, y)   
def factorial(n):
    """Returns the factorial of n."""
    return math.factorial(n)
## TThis will be printed when the script is imported in another script
print("I am OUTSIDE  main function of example.py")

## This will not be executed unless main() is called explicitly
## however if this script is executed directly, then main() will be called
def main():
    print("I am in  main function of example.py")
if __name__ == "__main__":
    main()
