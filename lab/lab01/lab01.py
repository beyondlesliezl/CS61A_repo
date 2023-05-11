def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    number=n
    temp=n
    if k==0:
        print(1)
    elif k==1:       
        print(f"{n}")
    else:
        while k>1:
            temp-=1
            number=number*temp
            k-=1
        print(number)

def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    x=str(y)
    number=len(x)-1
    sum=0   
    temp=0
    while number>=0:
        temp=y//(10**(number+1))
        sum=sum+(y//(10**number)-temp*10)
        number-=1
    return sum




def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    x=str(n)
    number=len(x)-1
    temp=0
    fre=0
    while number>=0:
        temp=n//(10**(number+1))
        if (n//(10**(number))-temp*10)==8:
            fre+=1

        number-=1  
    if fre==2:
        print("True")
    else:
        print("False") 
