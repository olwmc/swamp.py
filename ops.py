import random
import uuid

# HELPER FUNCTIONS
def not_none(x_y):
    if x_y[0] != None and x_y[1] != None:
        return True
    
    else:
        return False

def get_x_y(stack):
    y = POP(stack)
    x = POP(stack)

    return x,y

# INPUT
def INPUT(stack):
    inp = float(input())
    PUSH(inp, stack)

# SAVE
def SAVE_LOG(stack):
    # Output string
    outstr = ""
    
    # File name is the current date&time
    file_name = str(uuid.uuid4())[:8] + ".swampshot"

    # Build output string
    for element in stack:
        outstr += str(element) + "\n"

    # Write output string
    with open(file_name, "w") as f:
        f.write(outstr)

    # Print message
    print("Log saved: " + file_name)

# RNG
def RNDM(stack):
    num = POP(stack)
    PUSH(random.randint(0,num), stack)

# OPERATIONS
def ADD(stack):
    x_y = get_x_y(stack)
    
    if(not_none(x_y)):
        PUSH(x_y[0] + x_y[1], stack)

def SUB(stack):
    x_y = get_x_y(stack)
    
    if(not_none(x_y)):
        PUSH(x_y[0] - x_y[1], stack)

def MULT(stack):
    x_y = get_x_y(stack)
    
    if(not_none(x_y)):
        PUSH(x_y[0] * x_y[1], stack)

def DIV(stack):
    x_y = get_x_y(stack)
    
    if(not_none(x_y)):
        PUSH(x_y[0] / x_y[1], stack)

def MOD(stack):
    x_y = get_x_y(stack)
    
    if(not_none(x_y)):
        PUSH(x_y[0] % x_y[1], stack)

def PUSH(num, stack):
    if num % 1 == 0:
        stack.append(int(num))
    
    else:
        stack.append(num)

def POP(stack):
    try:
        ret = stack.pop()
        return ret
    except:
        print("Stack underflow")
        return None

def EQUALS(stack):
    x_y = get_x_y(stack)
    if x_y[0] == x_y[1]:
        PUSH(-1, stack)
    
    else:
        PUSH(0, stack)

def SWAP(stack):
    x_y = get_x_y(stack)

    PUSH(x_y[1], stack)
    PUSH(x_y[0], stack)

def OR(stack):
    x_y = get_x_y(stack)

    if x_y[0] == -1 or x_y[1] == -1:
        PUSH(-1, stack)

    else:
        PUSH(0, stack)

def AND(stack):
    x_y = get_x_y(stack)

    if x_y[0] == -1 and x_y[1] == -1:
        PUSH(-1, stack)

    else:
        PUSH(0, stack)

def GREATER_THAN(stack):
    x_y = get_x_y(stack)

    if x_y[0] > x_y[1]:
        PUSH(-1, stack)

    else:
        PUSH(0, stack)

def LESS_THAN(stack):
    x_y = get_x_y(stack)

    if x_y[0] < x_y[1]:
        PUSH(-1, stack)

    else:
        PUSH(0, stack)

def INVERT(stack):
    top = POP(stack)

    PUSH(top, stack)
    PUSH(-1, stack)
    MULT(stack)
    PUSH(1, stack)
    SUB(stack)
        
def DUP(stack):
    end = POP(stack)
    PUSH(end, stack)
    PUSH(end, stack)

def ROT(stack):
    n3 = POP(stack)
    n2 = POP(stack)
    n1 = POP(stack)

    PUSH(n2, stack)
    PUSH(n3, stack)
    PUSH(n1, stack)

def OVER(stack):
    # n1 n2 -- n1 n2 n1
    n2 = POP(stack)
    n1 = POP(stack)

    PUSH(n1, stack)
    PUSH(n2, stack)
    PUSH(n1, stack)

def EMIT(stack):
    n = POP(stack)
    print(chr(n), end="")

def CLEAR(stack):
    while stack:
        POP(stack)

def PRINT(stack):
    num = POP(stack)

    if num != None:
        print(num, end="")

def LIST(stack):
    print(stack)

def EXIT(stack):
    exit()

def RETURN(stack):
    print()
