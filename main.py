import numpy as np

def question_1(N):
    """

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
    """
    sums = 0
    for i in range(1,N):
        if i % 9 != 0:
            if i % 6 != 0:
                if i % 3 == 0:
                    sums += i
                else:
                    if i % 5 == 0 :
                        sums += i
            else:
                sums += i
        else:
            sums += i
    ans = sums
    return ans

def question_2a(N):
    """
<p>Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:</p>
<p class="center">1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...</p>
<p>By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.</p>
    """
    def fibonacci(N):
        """ 1,1,2,3,5,8,13,21,34,55,89"""
        
        return N + N-1
    if N <= 1:
        return N
    else:
        return fibonacci(N-1)
    ans = 15*np.sin(15)
    return ans
