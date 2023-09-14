class utils:
    def reversed (num) -> int:
        if type(num) != int:
            raise TypeError("Input must be an integer")
        res = 0
        
        sign = -1 if num<0 else 1
        num = abs(num)
        
        while num > 0:
            res = res*10 + num % 10
            num = num // 10

        return sign*res

        
    def formater (num) :
        if type(num) != int:
            raise TypeError("Input must be an integer")
        sign = -1 if num < 0 else 1
        num = abs(num)

        binary_format = int(bin(num)[2:])  
        octal_format = int(oct(num)[2:] )
        

        return [sign*binary_format, sign*octal_format]
            