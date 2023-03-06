# python3

import sys
import threading


def compute_height(n, parents):
    # Write this function
    max_height = 0
    # Your code here
    while n > 0:
        max_height += 1
        parents //= n
    return max_height

def main():
    # implement input form keyboard and from files
    # Accept int input for user input
    n = int(input)
    parents = int(input)
    max_height = compute_height(n, parents)
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    #with open("./directory/filename", mode="r"): as fails:
            #text = fails.read() 
    #print(text)
    # input number of elements
    print(max_height)
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
