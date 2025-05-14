'''
Problem statement
You have been given an integer 'N'.



Your task is to return true if it is a power of two. Otherwise, return false.



An integer 'N' is a power of two, if it can be expressed as 2 ^ 'K' where 'K' is an integer.



For example:
'N' = 4,
4 can be represented as 2^2. So, 4 is the power of two, and hence true is our answer.
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
16
Sample Output 1:
true
Explanation of Sample Input 1:
16 can be represented as 2^4. So, 16 is the power of two, and hence true is our answer.
Sample Input 2:
10
Sample Output 2:
false
Constraints:
-2^31 <= 'N' <= 2^31 - 1

Time Limit: 1sec
'''

def isPowerOfTwo(n:int) -> bool:
    if n<=0 :
        return False
    if n&(~(n-1))==n:
        return True
    
    return False