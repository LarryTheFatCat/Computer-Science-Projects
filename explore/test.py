
def f(x):
    num = input("Enter a number from 1-10: ")
    if num.isnumeric() == False:
        return 10
    elif num < 1:
        return 1
    elif num > 10:
        return 10
    else:
        return num
    
if __name__ = "__main__":
    
