#!python3
'''
This is a challenging problem!

x06. Determine the factored form
You may use the functions you created in previous assignments
'''
import x05_roots
import math

def Factored(a,b,c):
  '''
  input parameters:
  a, b, c: signed float
  These are the coefficients in the quadratic function ax^2 + bx + c = 0
  
  Write the equation in a nicely formatted factored form. This means no fractions
  
  return:
  list : 2 string literals representing the factors.  The order does not matter
  None if the quadratic can not be factored
  '''
  x = x05_roots.roots(a,b,c)
  if x == None:
    print("None Found")
    return None

  else:
    if x[0] %1 == 0:
      m = int(x[0])
    else:
      m = x[0]
    
    if x[1] %1 == 0:
      n = int(x[1]) 
    else:
      n = x[1]

    if m >= 0:
      if m % 1 != 0:
        for i in range (1,5):
          if a%i == 0 and m*a%i == 0:
            term1 = f"({int(a/i)}x + {int(m*a/i)})"

      else:
        term1 = f"(x - {int(m)})"

    else: 
      m = m*-1
      if a != 1:
        for i in range (1,5):
          if a%i == 0 and m*a%i == 0:
            term1 = f"({int(a/i)}x + {int(m*a/i)})"

      else: 
        term1 = f"(x + {int(m)})"
    
    if n >= 0:
      if n % 1 != 0:
        for i in range (1,5):
          if a%i == 0 and n*a%i == 0:
            term2 = f"({int(a/i)}x + {int(n*a/i)})"

      else:
        term1 = f"(x - {int(n)})"

    else: 
      n = n*-1
      if n % 1 != 0: 
        for i in range (1,5):
          if a%i == 0 and n*a%i == 0:
            term2 = f"({int(a/i)}x + {int(n*a/i)})"

      else:
        term2 = f"(x + {int(n)})"
    

    answer = [term1,term2]
    print(answer)
    return answer

def main():
  #print(Factored(1,1,-6))
  assert ("(x + 3)" in Factored(1,1,-6)) == True
  assert ("(x - 2)" in Factored(1,1,-6)) == True
  assert ("(x + 2)" in Factored(1,7,10)) == True
  assert ("(2x + 1)" in Factored(2,5,2)) == True
  assert ("(x + 2)" in Factored(2,5,2)) == True
  assert ("(3x + 1)" in Factored(6,-7,-3)) == True
  assert Factored(1,4,7) == None
  assert Factored(2,4,4) == None
  
if __name__ == "__main__":
  main()
  
