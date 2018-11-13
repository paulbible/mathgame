# simple sympy
import sympy
import random

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
    HardDegree1 = HcoefX + random.randint(1,20)
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

def main():
    print("1) SIMPLIFIED, LOW and ANY equation")
    print("2) SIMPLIFIED, HIGH and ANY equation")
    print("3) SIMPLIFIED, LOW and WHOLE equation")
    print("4) SIMPLIFIED, HIGH and WHOLE equation")
    print("5) UNSIMPLIFIED, LOW and ANY equation")
    print("6) UNSIMPLIFIED, HIGH and ANY equation")
    print("7) UNSIMPLIFIED, LOW and WHOLE equation")
    print("8) UNSIMPLIFIED, HIGH and WHOLE equation")
    flag = int(input("Choose an option"))
    
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

main()

# ALlOW NEGATIVE NUMBERS Answers
# GEN Question Function
# second degree questions
# simple factoring, solving for zeros, quadratic equation, completing the square
# in order of hardest first, 1.quadratic eq. 2. factoring 3. completing square

        


