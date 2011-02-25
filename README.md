    >>> import Sexpr
    >>> Sexpr.loads('()("a b)')
    [[], ['"a', 'b']]

    >>> Sexpr.puts([[], ['"a', 'b']])
    '(() ("a b))'

    >>> unstructured = ["Data",1,2,3]
    >>> try: a,b,c = Sexpr.unpack(unstructured,"Data")
    ... except IndexError: pass
    ... else: print c
    ... 
    3
    >>>
