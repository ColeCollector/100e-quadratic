#! python3

"""
**** The Discriminant
The square root part is called the "discriminant".  
1. Depending on the coefficients, it is possible for it to have a negative value. Since you can't square root a negative, when the discrminant is 0, there are no solutions to the equation.
2. If the discriminant is 0, there is only 1 solution, because the quadratic is a perfect square
3. If the discriminant is positive, there will be 2 solutions
4. If the discriminant is a perfect square, then the roots will be rational numbers (fractions) and it is possible to solve the quadratic by factoring rather than having to rely on the quadratic formula
5. If the discriminant is not a perfect square, then the roots will be irrational numbers (involving roots) and the quadratic can not be factored.

Assignments:
##### x01. Determine the value of the discriminant
Create a function that will return the value of the discriminant
input parameters:
a, b, c: signed float 
These are the coefficients in the quadratic equation. They may be positive or negative decimals

return value:
float
This will be a signed value for the discriminant. It may be positive or negative

"""

def discriminant(a,b,c):
  dis = (b**2)-(4*a*c)
  return dis


def main():
  assert discriminant(1,4,4) == 0
  assert discriminant(1,-1,-6) == 25
  assert discriminant(2,3,8) == -55
  
if __name__=="__main__":
  main()
