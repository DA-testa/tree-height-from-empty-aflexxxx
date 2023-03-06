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
    mode = input()
    if mode == 'F':
        # read input from file
        n = int(input())
        parents = list(map(int, input().split()))
    else:
        # read input from keyboard
        n = int(input())
        parents = list(map(int, input().split()))

    # compute tree height and print the result
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
