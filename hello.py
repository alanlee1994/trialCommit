import pandas as pd

def say_hello():
    print("hello")

def do_math(x,y):
    return x+y

if __name__ == "__main__":
    say_hello()
    x=1
    y=3
    print(do_math(x,y))