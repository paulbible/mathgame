# simple sympy
import sympy
import random
import math

x = sympy.symbols('x')
y = sympy.symbols('y')
z = sympy.symbols('z')

def Low_Any_Eq():
    n = random.randint(1,5)
    coefX= n*x
    simpleDegree1 = coefX + random.randint(1,10)
    expr = sympy.Eq(simpleDegree1, random.randint(1,10))
    return expr


def High_Any_Eq():
    n = random.randint(5,10)
    HcoefX = n*x
    HardDegree1 = HcoefX + random.randint(1,30)
    expr = sympy.Eq(HardDegree1, random.randint(1,30))
    return expr

def HardDegree1Eq2():
    expr = sympy.Eq(sympy.Add(HardDegree1(),HardDegree1(), evaluate=False) , random.randint(1,30))
    return expr

def Unsimplfied_LOW_ANY():
    n = random.randint(1,5)
    coefX= n*x
    simpleDegree1 = coefX + random.randint(1,10)

    G = random.randint(1,5)
    GcoefX= G*x
    GsimpleDegree1 = GcoefX + random.randint(1,10)
    
    expr = sympy.Eq(simpleDegree1, GsimpleDegree1)
    return expr

def Unsimplfied_HIGH_ANY():
    n = random.randint(5,10)
    HcoefX = n*x
    HardDegree1 = HcoefX + random.randint(1,20)
    
    G = random.randint(5,10)
    GHcoefX = G*x
    GHardDegree1 = GHcoefX + random.randint(1,20)
    
    expr = sympy.Eq(HardDegree1,GHardDegree1)
    return expr

def Low_Whole_Eq():
    #Ax + B = C
    n = random.randint(1,5)
    r = random.randint(1,5)
    coefX = n*x
    B = random.randint(1,10)
    simpleDegree1 = coefX + B
    C = B + n*r
    expr = sympy.Eq(simpleDegree1, C)
    return expr

def High_Whole_Eq():
    #Ax + B = C
    n = random.randint(5,10)
    r = random.randint(1,10)
    coefX = n*x
    B = random.randint(1,20)
    simpleDegree1 = coefX + B
    C = B + n*r
    expr = sympy.Eq(simpleDegree1, C)
    return expr

def Unsimplified_High_whole():
    #(n-r)x - rando = (n-r)rando - rando
    n = random.randint(9,16)
    r = random.randint(1,8)
    coefX = n*x
    HcoefX = r*x
    B = (n-r)*random.randint(1,10)
    C = random.randint(1,5)
    Right = coefX + C
    Left = HcoefX + C + B
    expr = sympy.Eq(Right, Left)
    return expr
    
def Unsimplified_Low_whole():
    #(n-r)x - rando = (n-r)rando - rando
    n = random.randint(4,6)
    r = random.randint(1,3)
    coefX = n*x
    HcoefX = r*x
    B = (n-r)*random.randint(1,4)
    C = random.randint(1,5)
    Right = coefX + C
    Left = HcoefX + C + B
    expr = sympy.Eq(Right, Left)
    return expr

def Simple_DEGREE2():
    n = random.randint(1,5)
    coefX= x*x
    simpleDegree1 = coefX
    expr = sympy.Eq(simpleDegree1, n*n)
    return expr

def UNSimple_DEGREE2():
    n = random.randint(1,5)
    coefX= n*x*x
    simpleDegree1 = coefX + random.randint(1,5)
    expr = sympy.Eq(simpleDegree1, random.randint(6,10))
    return expr

def ANSWER(questionType):
    print("#################")
    print("Solve")
    expr = questionType
    #print(expr)
    print(sympy.latex(expr))
    #print(sympy.solvers.solve(expr))
    ANS = sympy.solveset(expr)
    User = input()
    List = {User}
    if ANS == List:
        print("correct")
    else:
        print("incorrect")
        print(ANS)
    print("---------------")
    print()

def ANSWER2(questionType):
    print("#################")
    print("Solve")
    expr = questionType
    #print(expr)
    print(sympy.latex(expr))
    #print(sympy.solvers.solve(expr))
    ANS = sympy.solveset(expr)
    USER = str(input())
    USER2 = "-" + USER
    LIST = {USER2, USER}
    if ANS == LIST:
        print("correct")
    else:
        print("incorrect")
        print(ANS)
    print("---------------")
    print()
    
def MENUMODE(questionType):
    expr = questionType
    print(sympy.latex(expr))
    ANS = sympy.solveset(expr)
    print("1 is add, 2 is subtract, 3 is add multiples of X, and 4 is subtract multiples of X, 5 and 6 are divide and multiply, and 7 is to solve")
    CHOICE = int(input())
    if CHOICE == 1:
        n = ADD(expr)
        MENUMODE(n)
    elif CHOICE == 2:
        n = SUBTRACT(expr)
        MENUMODE(n)
    elif CHOICE == 3:
        n = ADDX(expr)
        MENUMODE(n)
    elif CHOICE == 4:
        n = SUBTRACTX(expr)
        MENUMODE(n)
    elif CHOICE == 5:
        n = Divide(expr)
        MENUMODE(n)
    elif CHOICE == 6:
        n = Multiply(expr)
        MENUMODE(n)
    elif CHOICE == 7:
        ANSWER(expr)
    
        
def ADD(expr):
    print("How much do you want to add")
    IN = int(input())
    Right = expr.rhs
    Left = expr.lhs
    OUT = sympy.Eq(Left+IN, Right+IN)
    return OUT
def ADDX(expr):
    print("How much do you want to add in multiples of x")
    IN = int(input())
    C = IN*x
    Right = expr.rhs
    Left = expr.lhs
    OUT = sympy.Eq(Left+C, Right+C)
    return OUT
def SUBTRACT(expr):
    print("How much do you want to subtract")
    IN = int(input())
    Right = expr.rhs
    Left = expr.lhs
    OUT = sympy.Eq(Left-IN, Right-IN)
    return OUT
def SUBTRACTX(expr):
    print("How much do you want to subtract in multiples of x")
    IN = int(input())
    C = IN*x
    Right = expr.rhs
    Left = expr.lhs
    OUT = sympy.Eq(Left-C, Right-C)
    return OUT
def Multiply(expr):
    print("How much do you want to multiply by")
    IN = int(input())
    Right = IN * expr.rhs
    Left = IN *expr.lhs
    OUT = sympy.Eq(Left, Right)
    return OUT
def Divide(expr):
    print("How much do you want to divide by")
    IN = int(input())
    Right = expr.rhs/IN
    Left = expr.lhs/IN
    OUT = sympy.Eq(Left, Right)
    return OUT

def GenQuestion():
    print("type in 0 for first option and 1 for second")
    print("degree 1 or 2 question or menumode is option 2")
    d = int(input("Choose an option"))
    if d == 0:
        print("simplified or unsimplified")
        f2 = int(input("Choose an option"))
        print("Low or High numbered")
        f3 = int(input("Choose an option"))
        print("Any or Whole answer")
        f4 = int(input("Choose an option"))
        if f2 == 0 and f3 == 0 and f4 == 0:
            x = 1
        elif f2 == 0 and f3 == 0 and f4 == 1:
            x = 3
        elif f2 == 0 and f3 == 1 and f4 == 1:
            x = 4
        elif f2 == 1 and f3 == 0 and f4 == 1:
            x = 7
        elif f2 == 1 and f3 == 1 and f4 == 1:
            x = 8
        elif f2 == 0 and f3 == 1 and f4 == 0:
            x = 2
        elif f2 == 1 and f3 == 0 and f4 == 0:
            x = 5
        elif f2 == 1 and f3 == 1 and f4 == 0:
            x = 6
    elif d == 1:
        print("simplified or unsimplified")
        d2 = int(input("Choose an option"))
        if d2 == 0:
            x = 9
        elif d2 == 1:
            x = 10
    elif d == 2:
        x = 11
        
    return x
def main():
    
    flag = GenQuestion()
    if flag == 0:
        print("NO QUESTION")
    if flag == 1:
        for i in range(5):
            ANSWER(Low_Any_Eq())
    elif flag == 2:
        for i in range(5):
            ANSWER(High_Any_Eq())
    elif flag == 3:
        for i in range(5):
            ANSWER(Low_Whole_Eq())
    elif flag == 4:
        for i in range(5):
            ANSWER(High_Whole_Eq())
    elif flag == 5:
        for i in range(5):
            ANSWER(Unsimplfied_LOW_ANY())
    elif flag == 6:
        for i in range(5):
            ANSWER(Unsimplfied_HIGH_ANY())
    elif flag == 7:
        for i in range(5):
            ANSWER(Unsimplified_Low_whole())
    elif flag == 8:
        for i in range(5):
            ANSWER(Unsimplified_High_whole())
    elif flag == 9:
        for i in range(5):
            ANSWER2(Simple_DEGREE2())
    elif flag == 10:
        for i in range(5):
            ANSWER2(UNSimple_DEGREE2())
    elif flag == 11:
        for i in range(5):
            MENUMODE(Unsimplified_Low_whole())
    
main()
        
# second degree questions
#--factoring problem
#
# negative solutions for last few problem types


