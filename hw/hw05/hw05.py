def make_bank(balance):
    """Returns a bank function with a starting balance. Supports
    withdrawals and deposits.

    >>> bank = make_bank(100)
    >>> bank('withdraw', 40)    # 100 - 40
    60
    >>> bank('hello', 500)      # Invalid message passed in
    'Invalid message'
    >>> bank('deposit', 20)     # 60 + 20
    80
    >>> bank('withdraw', 90)    # 80 - 90; not enough money
    'Insufficient funds'
    >>> bank('deposit', 100)    # 80 + 100
    180
    >>> bank('goodbye', 0)      # Invalid message passed in
    'Invalid message'
    >>> bank('withdraw', 60)    # 180 - 60
    120
    """
    def bank(message, amount):
        "*** YOUR CODE HERE ***"
        nonlocal balance
        if message=='withdraw':
            if balance>amount:
                balance-=amount
                return balance
            else:
                return 'Insufficient funds'
        if message=='deposit':
            balance+=amount
            return balance
        else:
            return 'Invalid message'
    return bank


def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> error = w(90, 'hax0r')
    >>> error
    'Insufficient funds'
    >>> error = w(25, 'hwat')
    >>> error
    'Incorrect password'
    >>> new_bal = w(25, 'hax0r')
    >>> new_bal
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Too many incorrect attempts. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Too many incorrect attempts. Attempts: ['hwat', 'a', 'n00b']"
    >>> type(w(10, 'l33t')) == str
    True
    """
    "*** YOUR CODE HERE ***"
    Incorrect_password =[]
    def new_bank(withdraw,local_password):
        nonlocal balance,Incorrect_password
        if len(Incorrect_password)>=3:
            error_sentence_first="Too many incorrect attempts. Attempts: ['"
            for i in range(len(Incorrect_password)):
                error_sentence_first+=Incorrect_password[i]
                if i <(len(Incorrect_password)-1):
                    error_sentence_first+="', '"
            error_sentence_first+="']"
            return error_sentence_first
        if local_password==password:
            if balance>=withdraw:
                balance-=withdraw
                return balance
            else:
                return 'Insufficient funds'
        else:
            Incorrect_password.append(local_password)
            return 'Incorrect password'
    return new_bank


def repeated(t, k):
    """Return the first value in iterator T that appears K times in a row. Iterate through the items such that
    if the same iterator is passed into repeated twice, it continues in the second call at the point it left off
    in the first.

    >>> lst = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(lst, 2)
    9
    >>> lst2 = iter([10, 9, 10, 9, 9, 10, 8, 8, 8, 7])
    >>> repeated(lst2, 3)
    8
    >>> s = iter([3, 2, 2, 2, 1, 2, 1, 4, 4, 5, 5, 5])
    >>> repeated(s, 3)
    2
    >>> repeated(s, 3)
    5
    >>> s2 = iter([4, 1, 6, 6, 7, 7, 8, 8, 2, 2, 2, 5])
    >>> repeated(s2, 3)
    2
    """
    assert k > 1
    "*** YOUR CODE HERE ***"
    temp_list=[]
    while True:
        new_value=next(t)
        if not temp_list:
            temp_list.append(new_value)
        else:
            if new_value!=temp_list[0]:
                del temp_list[1:]
                temp_list[0]=new_value
            else:
                temp_list.append(new_value)
                if len(temp_list)==k:
                    return new_value
def merge(incr_a, incr_b):
    """Yield the elements of strictly increasing iterables incr_a and incr_b, removing
    repeats. Assume that incr_a and incr_b have no repeats. incr_a or incr_b may be infinite
    sequences.

    >>> m = merge([0, 2, 4, 6, 8, 10, 12, 14], [0, 3, 6, 9, 12, 15])
    >>> type(m)
    <class 'generator'>
    >>> list(m)
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    >>> def big(n):
    ...    k = 0
    ...    while True: yield k; k += n
    >>> m = merge(big(2), big(3))
    >>> [next(m) for _ in range(11)]
    [0, 2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    iter_a, iter_b = iter(incr_a), iter(incr_b)
    next_a, next_b = next(iter_a, None), next(iter_b, None)
    "*** YOUR CODE HERE ***"
    #in order ,and no repetition 
    #compare
    while next_a is not None or next_b is not None:
        if next_a is None:
            yield next_b
            next_b = next(iter_b, None)
        elif next_b is None:
            yield next_a
            next_a = next(iter_a, None)
        else:
            if next_a < next_b:
                yield next_a
                next_a = next(iter_a, None)
            elif next_b < next_a:
                yield next_b
                next_b = next(iter_b, None)
            else:
                yield next_a
                next_a, next_b = next(iter_a, None), next(iter_b, None)


def make_joint(withdraw, old_pass, new_pass):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Too many incorrect attempts. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    #three possible ,1.incorrect password
    #2.too many incorrect attempts
    #3.Insufficient funds 
    #4.a number 
    #if I can make  a new  acount
    #the password can append,not only two or three
    #后来更改的函数，如果密码输入错误 仍然会影响原来的函数
    test_str=withdraw(0,old_pass)
    if type(test_str)==str:#incorrect password,too many incorrect attempts
        return test_str
    spare_pass=[old_pass]
    spare_pass.append(new_pass)
    def new_func(amount,final_pass):
        nonlocal spare_pass
        for test_pass in spare_pass:
            if test_pass==final_pass:
                return withdraw(amount,old_pass)
        return withdraw(amount,final_pass)
    return new_func


def remainders_generator(m):
    """
    Yields m generators. The ith yielded generator yields natural numbers whose
    remainder is i when divided by m.

    >>> import types
    >>> [isinstance(gen, types.GeneratorType) for gen in remainders_generator(5)]
    [True, True, True, True, True]
    >>> remainders_four = remainders_generator(4)
    >>> for i in range(4):
    ...     print("First 3 natural numbers with remainder {0} when divided by 4:".format(i))
    ...     gen = next(remainders_four)
    ...     for _ in range(3):
    ...         print(next(gen))
    First 3 natural numbers with remainder 0 when divided by 4:
    4
    8
    12
    First 3 natural numbers with remainder 1 when divided by 4:
    1
    5
    9
    First 3 natural numbers with remainder 2 when divided by 4:
    2
    6
    10
    First 3 natural numbers with remainder 3 when divided by 4:
    3
    7
    11
    """
    "*** YOUR CODE HERE ***"
    #给定自然数m，产生m个generator，第一个产生被m整除余0的数，第二个产生被m整除余1的数……
    #我的难点在于如何返回m个generator
    #nums_squared_gc = (num**2 for num in range(5))  this is a generator 
    #now ,my difficult is how to return more than one generator at the same time
    def generate_fun(i):
        return (x for x in naturals() if x%m==i)
    def all_generators():
        for y in range(m):
            yield generate_fun(y)
    return all_generators()




def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

