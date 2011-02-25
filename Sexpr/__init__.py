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

def puts( sx ):
    if isinstance(sx,str): return sx
    return "(" + " ".join( puts(x) for x in sx ) + ")"

def unpack( sx, type_sigil ):
    if sx[0]==type_sigil:
        return sx[1:]
    raise IndexError("pattern match failed")
