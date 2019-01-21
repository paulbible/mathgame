"""mathqtools generating random math problems
A collection of classes and functions for generating math problems.
"""
import sympy
import random


class SimplePoly1Generator(object):
    def __init__(self,):
        """Initializes Sympy symbols
        """
        self.x = sympy.symbols('x')
        self.y = sympy.symbols('y')
        self.z = sympy.symbols('z')

    def Low_Any_Eq(self):
        """Returns a simple first degree polynomial question with a small coefficient.
        :return: sympy expression
        """
        n = random.randint(1, 5)
        coefX = n * self.x
        simpleDegree1 = coefX + random.randint(1, 10)
        expr = sympy.Eq(simpleDegree1, random.randint(1, 10))
        return expr

    def High_Any_Eq(self):
        """Returns a first degree polynomial question with a medium coefficient.
        :return: sympy expression
        """
        n = random.randint(5, 10)
        HcoefX = n * self.x
        HardDegree1 = HcoefX + random.randint(1, 30)
        expr = sympy.Eq(HardDegree1, random.randint(1, 30))
        return expr

    def Low_Whole_Eq(self):
        """Returns a first degree polynomial question with a coefficient.
            The solution is a whole number.
        :return: sympy expression
        """
        # Ax + B = C
        n = random.randint(1, 5)
        r = random.randint(1, 5)
        coefX = n * self.x
        B = random.randint(1, 10)
        simpleDegree1 = coefX + B
        C = B + n * r
        expr = sympy.Eq(simpleDegree1, C)
        return expr

    def High_Whole_Eq(self):
        """Returns a first degree polynomial question with a medium coefficient.
            The solution is a whole number.
        :return: sympy expression
        """
        # Ax + B = C
        n = random.randint(5, 10)
        r = random.randint(1, 10)
        coefX = n * self.x
        B = random.randint(1, 20)
        simpleDegree1 = coefX + B
        C = B + n * r
        expr = sympy.Eq(simpleDegree1, C)
        return expr

    def Unsimplfied_LOW_ANY(self):
        """Returns a first degree polynomial question with a small coefficient.
            There are unknowns on each side of the equation.
        :return: sympy expression
        """
        n = random.randint(1, 5)
        coefX = n * self.x
        simpleDegree1 = coefX + random.randint(1, 10)

        G = random.randint(1, 5)
        GcoefX = G * self.x
        GsimpleDegree1 = GcoefX + random.randint(1, 10)

        expr = sympy.Eq(simpleDegree1, GsimpleDegree1)
        return expr

    def Unsimplfied_HIGH_ANY(self):
        """Returns a first degree polynomial question with a medium coefficient.
            There are unknowns on each side of the equation.
        :return: sympy expression
        """
        n = random.randint(5, 10)
        HcoefX = n * self.x
        HardDegree1 = HcoefX + random.randint(1, 20)

        G = random.randint(5, 10)
        GHcoefX = G * self.x
        GHardDegree1 = GHcoefX + random.randint(1, 20)

        expr = sympy.Eq(HardDegree1, GHardDegree1)
        return expr

    def Unsimplified_High_whole(self):
        """Returns a first degree polynomial question with a medium coefficient.
            There are unknowns on each side of the equation.
            The solution is a whole number
        :return: sympy expression
        """
        # (n-r)x - rando = (n-r)rando - rando
        n = random.randint(9, 16)
        r = random.randint(1, 8)
        coefX = n * self.x
        HcoefX = r * self.x
        B = (n - r) * random.randint(1, 10)
        C = random.randint(1, 5)
        Right = coefX + C
        Left = HcoefX + C + B
        expr = sympy.Eq(Right, Left)
        return expr

    def Unsimplified_Low_whole(self):
        """Returns a first degree polynomial question with a small coefficient.
            There are unknowns on each side of the equation.
            The solution is a whole number
        :return: sympy expression
        """
        # (n-r)x - rando = (n-r)rando - rando
        n = random.randint(4, 6)
        r = random.randint(1, 3)
        coefX = n * self.x
        HcoefX = r * self.x
        B = (n - r) * random.randint(1, 4)
        C = random.randint(1, 5)
        Right = coefX + C
        Left = HcoefX + C + B
        expr = sympy.Eq(Right, Left)
        return expr


class SimplePoly2Generator(object):
    def __init__(self):
        """Initializes Sympy symbols
        """
        self.x = sympy.symbols('x')
        self.y = sympy.symbols('y')
        self.z = sympy.symbols('z')

    def Simple_DEGREE2(self):
        """A simple degree 2 polynomial question.
        :return: sympy expression
        """
        n = random.randint(1, 5)
        coefX = self.x * self.x
        simpleDegree1 = coefX
        expr = sympy.Eq(simpleDegree1, n * n)
        return expr

    def UNSimple_DEGREE2(self):
        """A simple degree 2 polynomial question with coefficient.
        :return: sympy expression
        """
        n = random.randint(1, 5)
        coefX = n * self.x * self.x
        simpleDegree1 = coefX + random.randint(1, 5)
        expr = sympy.Eq(simpleDegree1, random.randint(6, 10))
        return expr
