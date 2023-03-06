# python3

import sys
import threading


# python3

import sys
import threading


def compute_height(n, parents):
    tree = [[] for i in range(n)]
    root = -1
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)

    def height(node):
        if not tree[node]:
            return 1
        else:
            return 1 + max([height(child) for child in tree[node]])

    return height(root)


def main():
    # take input from the user
    mode = input("Enter 'F' to read from file, 'I' to read from keyboard: ")
    while mode not in ['F', 'I']:
        print("Invalid input!")
        mode = input("Enter 'F' to read from file, 'I' to read from keyboard: ")

    if mode == 'F':
        # read input from file
        file_name = input("Enter file name: ")
        while 'a' in file_name:
            print("File name cannot contain 'a'!")
            file_name = input("Enter file name: ")
        with open(f'folder/{file_name}', 'r') as f:
            n = int(f.readline())
            parents = list(map(int, f.readline().split()))
    else:
        # read input from keyboard
        n = int(input())
        parents = list(map(int, input().split()))

    # compute tree height and print the result
    print(compute_height(n, parents))


sys.setrecursionlimit(10**7) 
threading.stack_size(2**27)   
threading.Thread(target=main).start()
