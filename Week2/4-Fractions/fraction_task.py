from fractions import Fraction


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __truediv__(self):
        return self.numerator / self.denominator

    def __add__(self, second):
        return Fraction((self.__truediv__() + second.__truediv__()), 1)

    def __sub__(self, second):
        return Fraction((self.__truediv__() - second.__truediv__()), 1)

    def __mul__(self, second):
        return Fraction((self.__truediv__() * second.__truediv__()), 1)

    def __eq__(self, second):
        return self.__truediv__() == second.__truediv__()
