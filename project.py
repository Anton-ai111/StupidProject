import os
import random

def banner():
    print("=====================================================")
    print("                     FILE PROJECT                    ")
    print("              [1]='+' [2]='-' [3]='*' [4]=':'        ")
    print("=====================================================")

def numberGen():
    return random.randint(1, 100)

def numberGen2():
    return random.randint(1, 1000)

def numberLive():
    v=numberGen()
    n=numberGen2()
    banner()
    g=input("[?]: ")
    if g == "1":
        h=v+n
        print("+" , v+n)
    elif g == "2":
        h=v-n
        print("-", v-n)
    elif g == "3":
        h=v*n
        print("*", v*n)
    elif g == "4":
        h=v/n
        print(": ", v/n)
    return h

def Os():
    file_path = "math.txt"
    fd = os.open(file_path, os.O_CREAT | os.O_WRONLY)
    combined_message = f"Hello, this file contains {numberLive()}!".encode("utf-8")
    os.write(fd , combined_message)
    os.close(fd)
    print(f"File '{file_path}' has been created.")

def Live():
    print("Bye")

def main():
    numberLive()
    Os()
    Live()

if __name__ == "__main__":
    while True:
        main()
