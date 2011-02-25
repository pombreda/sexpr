> Load S-expressions from a string
>    >>> import Sexpr
>    >>> Sexpr.loads('()("a b)')
>    [[], ['"a', 'b']]  
   
  
> Convert S-expressions to string representation
>    >>> Sexpr.puts([[], ['"a', 'b']])
>    '(() ("a b))'  
  
  
> Pattern match against sequential data types
>    >>> unstructured = ["Data",1,2,3]
>    >>> try: a,b,c = Sexpr.unpack(unstructured,"Data")
>    ... except IndexError: pass
>    ... else: print c
>    ... 
>    3
