
# A[] represents coefficients of first polynomial 
# B[] represents coefficients of second polynomial 
# m and n are sizes of A[] and B[] respectively 
  
# A utility function to print a polynomial 
def printPoly(poly, n): 
    for i in range(n): 
        print(poly[i], end = "") 
        if (i != 0): 
            print("x^", i, end = "") 
        if (i != n - 1): 
            print(" + ", end = "") 
  
# Driver Code 
if __name__ == '__main__': 
      
    # The following array represents 
    # polynomial 5 + 10x^2 + 6x^3 
    A = [5, 0, 10, 6] 
  
    # The following array represents 
    # polynomial 1 + 2x + 4x^2 
    B = [1, 2, 4] 
    m = len(A) 
    n = len(B) 
  
    print("First polynomial is") 
    printPoly(A, m) 
    print("\n", end = "") 
    print("Second polynomial is") 
    printPoly(B, n) 
    print("\n", end = "")  
    size = max(m, n) 
  
      
