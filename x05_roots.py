#!python3
'''
## SDSS Computing Studies Python Assignment
### Assignment #102a Quadratic Formula

#### Introduction
The quadratic formula is used in math to find the roots (solutions) for the equation ax^2 + bx + c = 0 where a, b and c are coefficients.  These roots also correspond to the x-intercepts when the function is graphed.

The quadratic formula is given by the equation: x = (-b +/- sqrt(b^2 - 4 * a * c)) / (2a)
A more visually friendly version can be found at many websites, including: https://magoosh.com/math/what-is-the-quadratic-formula/

There are a few items to note about the quadratic formula:
**** The Discriminant
The square root part is called the "discriminant".  
1. Depending on the coefficients, it is possible for it to have a negative value. Since you can't square root a negative, when the discrminant is 0, there are no solutions to the equation.
2. If the discriminant is 0, there is only 1 solution, because the quadratic is a perfect square
3. If the discriminant is positive, there will be 2 solutions
4. If the discriminant is a perfect square, then the roots will be rational numbers (fractions) and it is possible to solve the quadratic by factoring rather than having to rely on the quadratic formula
5. If the discriminant is not a perfect square, then the roots will be irrational numbers (involving roots) and the quadratic can not be factored.

Assignments:
x05. Determine the roots

Create a function that will determine the roots.
You may import the functions from your other assignments.
'''
import x01_discriminant
import math


def roots(a,b,c):
  '''
  input parameters:
  a, b, c : signed float
  coefficients for the quadratic in the format:
  ax^2 + bc + c = 0
  
  return:
  list with the 2 values of the roots if there are solutions
  None if there are no solutions
  '''
  x = x01_discriminant.discriminant(a,b,c)
  if x < 0: 
    return None

  else: 
    root = int((-b + round(math.sqrt(x)))/2)
    root2 = int((-b - round(math.sqrt(x)))/2)
    return (root,root2)
    


def main():
  assert (3 in roots(1,-1,-6)) == True
  assert (-2 in roots(1,-1,-6)) == True
  assert (-2 in roots(1,4,4)) == True
  assert roots(2,3,8) == None
  
if __name__ == "__main__":
  main()
  
