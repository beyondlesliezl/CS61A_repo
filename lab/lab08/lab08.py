def make_generators_generator(g):
    """Generates all the "sub"-generators of the generator returned by
    the generator function g.

    >>> def every_m_ints_to(n, m):
    ...     i = 0
    ...     while (i <= n):
    ...         yield i
    ...         i += m
    ...
    >>> def every_3_ints_to_10():
    ...     for item in every_m_ints_to(10, 3):
    ...         yield item
    ...
    >>> for gen in make_generators_generator(every_3_ints_to_10):
    ...     print("Next Generator:")
    ...     for item in gen:
    ...         print(item)
    ...
    Next Generator:
    0
    Next Generator:
    0
    3
    Next Generator:
    0
    3
    6
    Next Generator:
    0
    3
    6
    9
    """
    "*** YOUR CODE HERE ***"
    def gen_helper(num):
        gen=g()#then gen is a generator
        for i in range(num):
            yield(next(gen))
    count=len(list(g()))
    for i in range(count):
        yield(gen_helper(i+1))
            
    #I don't know how to use the innermost generators
    #return generator that the every_m_ints_to (n,m)
    #every(0,3),every(3,3),every(6,3)

