import re

def loads( s ):
    stack = [ [] ]
    for t in re.findall("\(|\)|[^\s\(\)]+", s):
        if t=="(": 
            stack.append( [] )
        elif t==")": 
            top = stack.pop()
            stack[-1].append( top )
        else:
            stack[-1].append( t )
    assert len(stack)==1
    return stack.pop()
