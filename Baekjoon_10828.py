import sys
N = int(sys.stdin.readline())
my_stack = []

def push(X):
    my_stack.append(X)

def pop():
    if len(my_stack) != 0:
        return my_stack.pop()
    else :
        return -1

def size():
    return len(my_stack)

def empty():
    if my_stack :
        return 0
    else :
        return 1
    
def top():
    if len(my_stack) != 0:
        return my_stack[-1]
    else :
        return -1
        
for _ in range(N):
    command = sys.stdin.readline().split()
    if command[0] == 'push':
        push(int(command[1]))
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'top':
        print(top())
    
