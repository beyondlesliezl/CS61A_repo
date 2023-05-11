HW_SOURCE_FILE=__file__


def pascal(row, column):
    """Returns a number corresponding to the value at that location
    in Pascal's Triangle.
    >>> pascal(0, 0)
    1
    >>> pascal(0, 5)	# Empty entry; outside of Pascal's Triangle
    0
    >>> pascal(3, 2)	# Row 4 (1 3 3 1), 3rd entry
    3
    """
    "*** YOUR CODE HERE ***"
    #超出Triangle范围返回0
    #row=column
    #pacal(row,column)=pascal(row-1,column)+pascal(row-1,column-1)
    if column>row or row<0 or column<0:
        return 0
    if row==0 and column==0:
        return 1
    else:
        return pascal(row-1,column)+pascal(row-1,column-1) 


def compose1(f, g):
    """"Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h

def repeated(f, n):
    """Return the function that computes the nth application of func (recursively!).

    >>> add_three = repeated(lambda x: x + 1, 3)
    >>> add_three(5)
    8
    >>> square = lambda x: x ** 2
    >>> repeated(square, 2)(5) # square(square(5))
    625
    >>> repeated(square, 4)(5) # square(square(square(square(5))))
    152587890625
    >>> repeated(square, 0)(5)
    5
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(HW_SOURCE_FILE, 'repeated',
    ...       ['For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"
    if n==0:
        return lambda x: x
    return compose1(f,repeated(f,n-1))


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    if x==0:
        return 0
    return num_eights(x//10)+(x%10==8)
    


def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(8)
    8
    >>> pingpong(10)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    -2
    >>> pingpong(30)
    -2
    >>> pingpong(68)
    0
    >>> pingpong(69)
    -1
    >>> pingpong(80)
    0
    >>> pingpong(81)
    1
    >>> pingpong(82)
    0
    >>> pingpong(100)
    -6
    >>> from construct_check import check
    >>> # ban assignment statements
    >>> check(HW_SOURCE_FILE, 'pingpong', ['Assign', 'AugAssign'])
    True
    """
    "*** YOUR CODE HERE ***"
    #special case :
    #1. n%8==0 2. num_eights(n)>0
    #我的问题在于如何确定是正在递增还是正在递减呢
    #肯定是返回前一个数的函数再加上1或者减去1
    #如果是正在递增，则返回上一个数的函数+1，如果是递减，则返回上一个数的函数-1
    def helper(i,value,direction):
        if i==n:
            return value 
        if num_eights(i)!=0 or i%8==0:
            return helper(i+1,value-direction,direction*-1)
        #用来改变方向
        else :
            return helper(i+1,value+direction,direction)
    return helper(1,1,1)
    #从起点开始往后递归，而不是从终点往前递归
    #启示：如果只有一个参数不够反应情况，那么就可以再重新定义一个函数