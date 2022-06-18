from typing import Union


class Variable:
    def __init__(self, v):
        self.var = v

    def __str__(self):
        return str(self.var)

    def sub(self, y, t):
        if self.var == y:
            return t
        return self

    def beta(self):
        return self


class Constant:
    def __init__(self, c):
        self.item = c

    def __str__(self):
        return str(self.item)

    def sub(self, y, t):
        return self

    def beta(self):
        return self


class Combination:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def __str__(self):
        """add "( )" """
        return "({} {})".format(self.m, self.n)

    def sub(self, y, t):
        return Combination(self.m.sub(y, t), self.n.sub(y, t))

    def alpha(self, y):
        return Combination(self.m.alpha(y), self.n.alpha(y))

    def beta(self):
        if isinstance(self.m, Combination):
            return Combination(self.m.beta(), self.n)

        if isinstance(self.m, Abstraction):
            return self.m.s.sub(self.m.x, self.n)

        if isinstance(self.n, Abstraction) or isinstance(self.n, Combination):
            return Combination(self.m, self.n.beta())

        return self

    def eta(self):
        """(λx.M x) N --> M N"""
        if isinstance(self.m, Abstraction):
            if isinstance(self.m.s, Combination):
                if self.m.x == self.m.s.n:
                    return Combination(self.m.s.m, self.n)


class Abstraction:
    """λx.s init"""
    def __init__(self, x, s):
        self.x = x
        self.s = s

    def __str__(self):
        return "λ{}.{}".format(self.x, self.s)

    def sub(self, y, t):
        if y == self.x:
            return self
        return Abstraction(self.x, self.s.sub(y, t))

    def alpha(self, y):
        if self.x == y:
            return self
        return Abstraction(y, self.s.sub(self.x, y))

    def beta(self):
        return Abstraction(self.x, self.s.beta())

    def eta(self):
        return Abstraction(self.x, self.s.eta())


TRUE = Abstraction('x', Abstraction('y', Variable('x')))
FALSE = Abstraction('x', Abstraction('y', Variable('y')))


def func_and(m: Abstraction, n: Abstraction) -> Combination:
    """logic and"""
    return Combination(Combination(m, n), FALSE)


def func_or(m: Abstraction, n: Abstraction) -> Combination:
    """logic or"""
    return Combination(Combination(m, TRUE), n)


def func_not(m: Abstraction) -> Combination:
    """logic not"""
    return Combination(Combination(m, FALSE), TRUE)


def number_n(n: int) -> Union[Combination, Variable]:
    if n > 0:
        return Combination(Variable('f'), number_n(n - 1))
    elif n == 0:
        return Variable('x')


def func_numbers(n: int) -> Abstraction:
    """create number"""
    return Abstraction('f', Abstraction('x', number_n(n)))


def func_succ(n: Abstraction) -> Abstraction:
    """n++"""
    return Abstraction('f', Abstraction('x', Combination(
        Variable('f'), Combination(Combination(
            n, Variable('f')), Variable('x')))))


def func_pred(n: Abstraction) -> Abstraction:
    """n--"""
    return Abstraction('f', Abstraction('x', Combination(
        Combination(Combination(n, Abstraction('g', Abstraction(
            'h', Combination(Variable('h'), Combination(Variable(
                'g'), Variable('f')))))), Abstraction(
            'u', Variable('x'))), Abstraction('u', Variable('u')))))


def func_plus(m: Abstraction, n: Abstraction) -> Abstraction:
    """m + n"""
    return Abstraction('f', Abstraction('x', Combination(
        Combination(m, Variable('f')), Combination(Combination(
            n, Variable('f')), Variable('x')))))


def func_multiply(m: Abstraction, n: Abstraction) -> Abstraction:
    """m * n"""
    return Abstraction('f', Combination(m, Combination(n, Variable('f'))))


def calculus(lam: Union[Abstraction, Combination]) -> Abstraction:
    print('-----------------------------------')
    while True:
        print(lam)
        temp = lam.beta()
        if str(lam) == str(temp):
            break
        lam = temp
    return lam
