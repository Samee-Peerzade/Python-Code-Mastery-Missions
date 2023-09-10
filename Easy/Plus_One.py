"""  
66. Plus One
Easy
8.2K
5.1K
Companies
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].



"""


#1) Reverse the digits 123=>321
#2) one=1 (carry) and index=0 
#3) while loop when one=1


def plusone(digits):
    digits=digits[::-1]
    one=1,
    index=0    
    
    while one:
        if index<len(digits):
            
            if digits[index]==9: #special case
                digits[index]=0
            else:                   
                digits[index]+=1   
                one=0                          #no carry
                
        else:  #index out of range
            digits.append(1)
            one=0
        index+=1 
        
    return digits[::-1]  #undo reverse


print(plusone([1,2,3]))
print(plusone([9]))      
                
                
                
                
                
                
                
        
    
    
    