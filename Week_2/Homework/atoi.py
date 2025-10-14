class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        #acts as a flag for +ve and -ve
        result = 0
        n = len(s)
        INT_MAX = (2**31) - 1
        i=0
        #we're using these notations since we're trying to convert it to a 
        #32bit signed integer
        INT_MIN = 2**(-31)

        while i<n and s[i] == ' ':
            i = i+1
        #skipping whitespaces entirely
        
        if i<n and s[i] == '+':
            sign = +1
            i = i+1
        #if the first sign is +ve
        
        elif i<n and s[i] == '-':
            sign = -1
            i = i+1
        #if the first sign is -ve

        while i<n and s[i].isdigit():
            digit = int(s[i])

            if(result > INT_MAX // 10) or (result == INT_MAX//10 and digit>INT_MAX%10):
                return INT_MAX if sign == 1 else INT_MIN

            #so the logic here is that if the result is greater than 2147483648
            #OR
            # if the result is equal to 2147483648 and the next number's greater than 7,
            #any digit appended to the result would be greater than INT_MAX provided
            #the sign is 1
            # if any of these conditions fail, it's then technically INT_MIN since INT_MAX and INT_MIN
            #are the same value (ignoring the sign) after the floor division


            #instead of digit>INT_MAX%10 , we can just write digit>7
            
            
            result = 10*result + digit
            #for the last number
            i += 1
            #updating pointer

        return sign * result