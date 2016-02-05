# Math library
# Author: Sébastien Combéfis
# Version: February 2, 2016
import math

def fact(n):
    """Computes the factorial of a natural number.
    
    Pre: -
    Post: Returns the factorial of 'n'.
    Throws: ValueError if n < 0.
    """
    R= math.factorial(n)
    return R

def roots(a, b, c):
    """Computes the roots of the ax^2 + bx + x = 0 polynomial.
    
    Pre: -
    Post: Returns a tuple with zero, one or two elements corresponding
          to the roots of the ax^2 + bx + c polynomial.
    """
    if a==0 and b==0:
        return None
    
    if a==0:
        RS= -c/b
        return (RS)
    
    D = b**2 - 4*a*c
    if D < 0:
        return None
    elif D == 0:
        R0 = (-b)/(2*a)
        return R0
    else:
        R1= (-b - math.sqrt(D))/(2*a)
        R2= (-b + math.sqrt(D))/(2*a)
        return (R1, R2)

def integrate(function, lower, upper):
    """Approximates the integral of a fonction between two bounds
    
    Pre: 'function' is a valid Python expression with x as a variable,
         'lower' <= 'upper',
         'function' continuous and integrable between 'lower‘ and 'upper'.
    Post: Returns an approximation of the integral from 'lower' to 'upper'
          of the specified 'function'.
    """
    steps= 5000
    h= (upper-lower)/steps
    x= lower

    integral= 0
    while x < upper:
        integral+= eval(function)*h
        x+= h
    return integral

if __name__ == '__main__':
    print(fact(5))
    print(roots(0, -4, 20))
    print(integrate('x ** 2 - 1', -1, 1))
    print(integrate('x', 0, 4))
